# main program that drives the program
import os
import requests
import json
import re
import pandas as pd

from dotenv import load_dotenv
from astrapy import DataAPIClient
from astrapy.constants import VectorMetric
from langchain_openai import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document
from uuid import uuid4

from nvd_api import *
from astra_database import *

def urls_retriever(ref_urls: list, cve_id: str) -> list:
    """
        Retrieve urls from the Vuln_Notification_Coding csv and from the reference urls from NVD API

        Args:
            ref_urls (list): list of reference urls from NVD API
            cve_id (str): cve_id

        Returns:
            list: list of urls to scrape vulnerability information from
    """
    df = pd.read_csv("New_Vuln_Notification_Coding.csv")
    cve_df = df[df['CVE'] == cve_id[4:]]
    urls_s = set()
    for val in cve_df['URL']:
        urls_s.add(val)

    urls = list(urls_s)
    urls.extend(ref_urls)

    return urls

def nvd_data_processor(cve_id: str, nvdapi_key: str) -> tuple[Document, list]:
    """
        Process NVD data for a given CVE ID.

        Args:
            cve_id (str): The CVE ID to process (e.g., 'CVE-2021-34527').
            nvdapi_key (str): The API key for accessing the NVD API.

        Returns:
            Document: An object containing the processed NVD information.
    """
    start = cve_id[4:]
    url = f'https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}'
    headers = {'apiKey': nvdapi_key}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"{cve_id} is not found on the NVD website")

    nvd_info = response.json()

    # print(json.dumps(nvd_info, indent=4))
    nvd_text = get_nvd_vuln_description(nvd_info)
    nvd_score = get_cvss_data(nvd_info)
    nvd_config = get_known_software_config(nvd_info)
    ref_url = get_references(nvd_info)
    nvd_text += str(nvd_score)
    nvd_text += str(nvd_config)

    nvd_doc = Document(
        page_content=nvd_text,
        metadata={
            'title': "",
            'url': url,
            'description': "NVD API Vulnerability Description",
            'keywords': "",
            'CVE': cve_id,
        }
    )

    return nvd_doc, ref_url


def main_driver(cve_id: str) -> tuple[list, list]:
    load_dotenv()

    nvd_api_key = os.getenv('NVD_API_KEY')

    nvd_dc, nvd_urls = nvd_data_processor(cve_id, nvd_api_key)
    urls = urls_retriever(nvd_urls, cve_id)
    vul_docs, nessus_docs = database_init(cve_id)

    vul_docs.append(nvd_dc.page_content)
    vul_docs.extend(urls)

    return vul_docs, nessus_docs


