"""adds nessus data to astradb using the same database but a different collection
    called nessus_collection"""

from random_data import *
import json
from langchain_core.documents import Document
from astra_database import *
from dotenv import load_dotenv
from astrapy.info import CollectionVectorServiceOptions
from astrapy import DataAPIClient
from astrapy.constants import VectorMetric
from langchain_openai import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore

def document_generator(data_json, docs_lst):
    for item in data_json:
        sections = []
        if item.get('synopsis'):
            sections.append(f"SYNOPSIS: {item['synopsis']}")
        if item.get('description'):
            sections.append(f"DESCRIPTION: {item['description']}")
        if item.get('solution'):
            sections.append(f"SOLUTION: {item['solution']}")

        page_content = "\n".join(sections) if sections else "No vulnerability information available"
        # Create metadata (excluding text fields)
        metadata = {k: v for k, v in item.items()
                    if k not in ['synopsis', 'description', 'solution'] and v is not None}

        doc = Document(
            page_content=str(item),
            metadata=metadata
        )
        docs_lst.append(doc)

    return docs_lst



if __name__ == '__main__':
    with open('data.json', 'r') as f:
        data = json.load(f)

    # print(type(data))
    docus = []
    documents = document_generator(data, docus)
    load_dotenv()

    astradb_token = os.getenv("ASTRA_DB_TOKEN")
    astradb_endpoint = os.getenv("ASTRA_DB_ENDPOINT")
    astradb_collection = "nessus_collection"
    astradb_namespace = os.getenv("ASTRA_DB_NAMESPACE")
    api_key = os.getenv("OPENAI_API_KEY")

    client = DataAPIClient(astradb_token)
    database = client.get_database(astradb_endpoint, keyspace=astradb_namespace)
    collection = database.get_collection(astradb_collection)

    openai_vectorize_options = CollectionVectorServiceOptions(
        provider="openai",
        model_name="text-embedding-ada-002",
        authentication={
            "providerKey": "openai_api_key",
        },
    )
    vector_store = AstraDBVectorStore(
        collection_name=astradb_collection,
        api_endpoint=astradb_endpoint,
        token=astradb_token,
        namespace=astradb_namespace,
        collection_vector_service_options=openai_vectorize_options,
    )

    vector_store.add_documents(documents)

