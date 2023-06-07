from base import Base
from dotenv import load_dotenv
import pymongo
import os
import pandas as pd

class ToMongo:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        
    def connect_to_mongo(self):
        load_dotenv()
        mongo_url = os.getenv('MONGO_URL')
        client = pymongo.MongoClient(mongo_url)
        db = client.db
        return db
    
    def upload_collection(self):
        db = self.connect_to_mongo()
        db.collection.insert_many(self.df.to_dict('records'))


if __name__ == '__main__':
    base_csv_file = r'C:\Users\RedneckRandy\Documents\GitHub\Student-Performance_data\student-por.csv'
    c = ToMongo(base_csv_file)
    print('Successful connection to client object')
    c.upload_collection()
    
    print('Data has been successfully uploaded to the MongoDB instance')
