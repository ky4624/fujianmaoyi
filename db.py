import pymongo
import sqlite3


class sqliter:
    def __init__(self):
        self.conn = sqlite3.connect('fujianmaoyi.db3')
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.conn.close()


class mongoer:
    def __init__(self,db_name):

        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

        self.db = self.client[db_name]
        
    def __del__(self):
        self.client.close()

       