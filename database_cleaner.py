"""sample code to clean the Astra database"""
import os
from dotenv import load_dotenv
from astrapy.info import CollectionVectorServiceOptions
from astrapy import DataAPIClient
from astrapy.constants import VectorMetric
from langchain_openai import OpenAIEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain_core.documents import Document

if __name__ == '__main__':
    load_dotenv()

    astradb_token = os.getenv("ASTRA_DB_TOKEN")
    astradb_endpoint = os.getenv("ASTRA_DB_ENDPOINT")
    astradb_collection = "nessus_collection"
    astradb_namespace = os.getenv("ASTRA_DB_NAMESPACE")

    client = DataAPIClient(astradb_token)
    database = client.get_database(astradb_endpoint, keyspace=astradb_namespace)
    collection = database.get_collection(astradb_collection)

    for i in range(101):
        collection.delete_many(filter={'metadata.severity.id':f"{i}"})

