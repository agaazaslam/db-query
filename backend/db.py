import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")







def connection():
    client = None 

    if not MONGO_URI:
        print("no uri check env")
        return 

    try:
        client = MongoClient(MONGO_URI)
        db = client["mydatabase"]
        collection = db["sample_user"]
        collection_2 = db["1mb_users"]
        collection_3 = db["credit-users"]


        client.admin.command('ping')
        print("Successfully connected to mongo")

        ## Query for the db 
        data = scanfile('credit-data.json')
        result = collection_3.insert_many(data)
        print("inserted successfully ")




    except Exception as e :
        print(f"unexpected error {e}")

    finally:
        if 'client' in locals() :
            client.close()
            print("Connections Closed")

def scanfile(file_path):
    with open(file_path,"r" ) as file:
        data = json.load(file)
        return data

def find_all(collection):
    for entry in collection.find({} , {"name":1 , "language":1  }):
        print(entry)

def group_by_language(collection):
    query = {"$group": {"_id": "$language", "count": {"$sum": 1}}  }
    sort = {"$sort":{"count":-1}}

    pipeline = [query , sort ]

    for c in collection.aggregate(pipeline):
        print(c)

def query_with_pipeline(collection , pipeline):
    result = collection.aggregate(pipeline)
    return result


def close_db():
    if 'client' in locals():
        client.close()
        print("Connections Closed")


def main():

    print("Hello from backend!")


if __name__ == "__main__":
    main()
    connection()

