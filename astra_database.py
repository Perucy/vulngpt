import os
from dotenv import load_dotenv
#from astrapy.info import CollectionVectorServiceOptions
from astrapy import DataAPIClient
from astrapy.constants import VectorMetric
from langchain_openai import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document


def database_search(collection, cve_id: str) -> list:
    hits_ite = collection.find(
        filter={'metadata.CVE': cve_id},
        projection={'_id': True, '$vectorize': True, 'metadata': True},
    )

    relevant_docs = []

    for d in hits_ite:
        relevant_docs.append(d['$vectorize'])

    doc_set = set()
    unique_docs = []

    for doc in relevant_docs:
        if doc not in doc_set:
            unique_docs.append(doc)
        doc_set.add(doc)

    return unique_docs


def database_init(cve_id: str) -> tuple[list,list]:
    load_dotenv()

    astradb_token = os.getenv("ASTRA_DB_TOKEN")
    astradb_endpoint = os.getenv("ASTRA_DB_ENDPOINT")
    astradb_collection = os.getenv("ASTRA_DB_COLLECTION")
    astradb_namespace = os.getenv("ASTRA_DB_NAMESPACE")

    client = DataAPIClient(astradb_token)
    database = client.get_database(astradb_endpoint, keyspace=astradb_namespace)
    vul_collection = database.get_collection(astradb_collection)
    nessus_collection = database.get_collection("nessus_collection")

    vul_docs = database_search(vul_collection, cve_id)
    nessus_docs = database_search(nessus_collection, cve_id)

    return vul_docs, nessus_docs


