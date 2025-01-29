import sys
import os
import json
import certifi

from dotenv import load_dotenv

load_dotenv()

MOGO_DB_URL=os.getenv("")

ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from NetworkSecurity.Exception.exception import NetworkSecurityException
from NetworkSecurity.Logging.logger import logging



# MongoDB URL (adjust this based on your setup)
MONGO_DB_URL = ''

class NetworkDataExtract:
    def __init__(self):
        try:
            
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            # Read CSV file
            data = pd.read_csv(file_path)
            
            # Reset index to avoid any issues with the original row indices
            data.reset_index(drop=True, inplace=True)
            
            # Convert DataFrame to JSON format (list of dictionaries)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            # Initialize MongoDB client and get database and collection
            mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            db = mongo_client[database]
            col = db[collection]

            # Insert records into MongoDB
            col.insert_many(records)
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    # Define your file path, MongoDB database, and collection names
    FILE_PATH = 'your_file_path_here.csv'  # Example: 'data.csv'
    DATABASE = 'your_database_name'        # Example: 'network_data'
    COLLECTION = 'your_collection_name'    # Example: 'data_records'
    
    # Create an instance of the NetworkDataExtract class
    networkobj = NetworkDataExtract()
    
    # Convert CSV to JSON
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    
    # Insert records into MongoDB
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    
    # Print the number of records inserted
    print(f"Inserted {no_of_records} records into MongoDB.")
