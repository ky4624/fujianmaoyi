import pymongo
import requests
from lxml import etree
import math
from db import mongoer,sqliter
from config import db_name, collection_name, indexurl,cookies,headers,mother
from concurrent.futures import ThreadPoolExecutor
import re

class indexer:
    def __init__(self):
        self.cl = mongoer(db_name,collection_name)
        self.db = self.cl.db
        self.collection = self.cl.collection
        self.count = 0

    def visit(self, url):
        pagef = int((int(re.findall(r'start=(.*?)&sz', url)[0])-1)/mother)
        for i in range(5):
            print(f'爬取网页第{pagef}页第{i}次')
            response = requests.get(url, cookies=cookies, headers=headers,  timeout=100)
            print(response.status_code)
            if "row product-grid" in response.text:
                return response.text
        return None

    def start(self):
        page0 = 0
        url = indexurl.format(page0)
        text = self.visit(url)
        ht = etree.HTML(text)
        self.count = int(ht.xpath('//span[contains(@class,"search-result-count")]')[0].text.replace(',','').replace('Results','').strip())
        self.collection.insert_one({"page": page0, "text": text, "url": url})
        pages = math.ceil(self.count/mother)+1

        #单线程
        # for page in range(1,pages):
        #     print(f'爬取网页第{page+1}页')
        #     url = indexurl.format(page*mother+1)
        #     text = self.visit(url)
        #     self.collection.insert_one({"page": page, "text": text, "url": url})

        #多线程
        urls = []
        for page in range(1,pages):
            url = indexurl.format(page*mother+1)
            urls.append(url)
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(self.visit, urls)
        res = [{"page": page1, "text": text1, "url": url1} for url1,page1, text1 in zip(urls, range(1,pages), results)]
        
        self.collection.insert_many(res)



    def paser(self):
        datas = self.collection.find().to_list()

        for data in datas:
            text = data['text']
            ht = etree.HTML(text)

        

    def main(self):
        ym = int(input('请输入要执行的操作：\n1. 爬取网页\n2. 解析网页\n请选择下标:'))
        if ym==1:
            self.start()
        elif ym==2:
            self.paser()
        print('已完成')

if __name__ == "__main__":
    indexer = indexer()
    indexer.main()
