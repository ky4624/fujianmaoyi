import pymongo
import sqlite3
from config import savedir

class sqliter:
    def __init__(self):
        self.conn = sqlite3.connect(f'{savedir}fujianmaoyi.db3')
        self.cursor = self.conn.cursor()
        self._create_table()
        self._create_down()

    def _create_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS fujianmaoyi (
            ID INTEGER,
            已采 TINYINT(1),
            已发 TINYINT(1),
            产品面包屑 TEXT,
            产品名称 TEXT,
            产品型号 TEXT,
            产品价格 TEXT,
            产品图片 TEXT,
            产品描述 TEXT,
            品牌 TEXT,
            产品特价 TEXT,
            细节图 TEXT,
            属性值1 TEXT,
            面包屑1 TEXT,
            sx名1 TEXT,
            sx值1 TEXT,
            sx名2 TEXT,
            sx值2 TEXT,
            sx名3 TEXT,
            sx值3 TEXT,
            sx名4 TEXT,
            sx值4 TEXT,
            描述1 TEXT,
            描述2 TEXT,
            PageUrl TEXT
        )
        """
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def _create_down(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS fujianmaoyi_down (
            id INTEGER,
            PreUrl VARCHAR(1000),
            TrueUrl VARCHAR(1000),
            SaveUrl VARCHAR(1000),
            ReplaceUrl VARCHAR(1000),
            Status TINYINT(1),
            Upload TINYINT(1),
            Type VARCHAR(1000),
            PageUrl VARCHAR(1000),
            ContentId INTEGER
     
        )
        """
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def insermany(self,datas,table):
        keys = ", ".join(datas[0].keys())
        values = ", ".join([f":{k}" for k in datas[0].keys()])
        sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        self.cursor.executemany(sql, datas)
        self.conn.commit()

    
    def __del__(self):
        self.conn.close()


class mongoer:
    def __init__(self,db_name):

        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

        self.db = self.client[db_name]
        
    def __del__(self):
        self.client.close()

       