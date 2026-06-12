# -*- coding: utf-8 -*-
import requests
from lxml import etree
import math
from db import mongoer,sqliter
from config import *
from concurrent.futures import ThreadPoolExecutor
import re
import json
import time
import re


class indexer:
    def __init__(self):
        self.cl = mongoer(db_name)
        self.db = self.cl.db
        self.collection = self.db[collection_name]
        self.collection_find = self.db[collection_find_name]
        self.source = []
        self.count = 0

        self.sqlite = sqliter()

    def visit(self, url):
        pagef = int((int(re.findall(r'start=(.*?)&sz', url)[0])-1)/mother)+1
        for i in range(5):
            response = requests.get(url, cookies=cookies, headers=headers,  timeout=100)
            print(f'爬取网页第{pagef}页第{i}次,状态码{response.status_code}')
            if "row product-grid" in response.text:
                return response.text
        return None

    def start(self):
        page0 = 0
        url = indexurl.format(page0)
        text = self.visit(url)
        ht = etree.HTML(text)
        self.count = int(ht.xpath('//span[contains(@class,"search-result-count")]')[0].text.replace(',','').replace('Results','').strip())
        self.collection.insert_one({"page": page0+1, "text": text, "url": url})
        pages = math.ceil(self.count/mother)+1

        #单线程
        # for page in range(1,pages):
        #     print(f'爬取网页第{page+1}页')
        #     url = indexurl.format(page*mother+1)
        #     text = self.visit(url)
        #     self.collection.insert_one({"page": page, "text": text, "url": url})

        #多线程
        urls = []
        results = []
        for page in range(1,pages):
            url = indexurl.format(page*mother+1)
            urls.append(url)
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(self.visit, urls)
        res= []
        for url1, text1 in zip(urls, results):
            res.append({"page": int((int(re.findall(r'start=(.*?)&sz', url1)[0])-1)/mother)+1, "text": text1, "url": url1})
            if len(res)==1000:
                self.collection.insert_many(res)
                res = []
        self.collection.insert_many(res)
        res = []
   

    def visitDetail(self,item0):
        url = item0['Detailurl']
        time.sleep(5)
        for i in range(5):
            response = requests.get(url, cookies=cookies_find, headers=headers_find,  timeout=100)
            print(f'爬取详情页第{i}次,状态码{response.status_code}')
            if "Bopis-GetDeliveryOption" in response.text:
                self.saveDetail(item0,json.loads(response.text))
                return response.json()
        return None

    def saveDetail(self,item0,item1):
        item1.update(item0)
        self.source.append(item1)

    def paser(self):
        find_list = []
        datas = self.collection.find().to_list()
        for data in datas:
            html = data['text']
            ht = etree.HTML(html)
            for item in ht.xpath('//a[contains(@class,"pdpLink")]'):
                item1 = {}
                url = item.get('href')
                proName = url.split('/')[-2]
                proNo = url.split('/')[-1].split('.')[0]
                indexFindUrlq = indexFindUrl.format(proName, proNo)
                item1['url'] = indexFindUrlq
                item1['pid'] = proNo
                item1['Detailurl'] = findurl.format(proNo, proNo, proNo, proNo, proNo, proNo, proNo, proNo, proNo)
                find_list.append(item1)



        #单线程
        # for finditem in find_list:
        #     self.visitDetail(finditem)

        #多线程
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(self.visitDetail, find_list)

        source = []
        for sour in self.source:
            source.append(sour)
            if len(source)==1000:
                self.collection_find.insert_many(source)
                source = []
        self.collection_find.insert_many(source)


    def save(self):
        no = 0
        down_no = 0
        results = []
        down_results = []
        datas = self.collection_find.find().to_list()
        for data in datas:
            detailData = data['products'][data['pid']]['availProduct']
            no += 1
            print(data['pid'])
            mianbaoxue = ''
            item = {}
            item['ID'] = no
            item['已采'] = 1
            item['已发'] = 0
            item['产品面包屑'] = mianbaoxue
            item['产品名称'] = detailData['productName']
            item['产品型号'] = detailData['masterID']


            if  detailData['price'].get('sales'):
                if not detailData['price']['sales']['formatted']:
                    continue
                item['产品价格'] = detailData['price']['sales']['formatted'].replace('$','')
            else:
                item['产品价格'] = detailData['price']['min']['sales']['formatted'].replace('$','')

            imgeitem = detailData.get('images')
            item['产品图片'] = ''
            if imgeitem:
                for itemk in imgeitem.keys():
                    imgs = imgeitem[itemk]
                    if imgs:
                        down_no += 1
                        imgurl = imgs[0]['url']
                        ite = {}
                        ite['id'] = down_no
                        ite['PreUrl'] = imgurl
                        ite['TrueUrl'] = imgurl
                        ite['SaveUrl'] = f"{img}{imgname}{no}.jpg"
                        ite['ReplaceUrl'] = f"{imgname}{no}.jpg"
                        ite['Status'] = 1
                        ite['Upload'] = 0
                        ite['Type'] = '产品图片'
                        ite['PageUrl'] = data['url']
                        ite['ContentId'] = no
                        down_results.append(ite)
                        if len(down_results)==1000:
                            self.sqlite.insermany(down_results,table_down)
                            down_results = []
                        item['产品图片'] = f"{imgname}{no}.jpg"
                        break
            
            description = detailData['longDescription']
            description_ = re.sub(r'<.*?>','',description)
            
            item['产品描述'] = description_
            item['品牌'] = ''
            item['产品特价'] = ''
            item['细节图'] = ''
            item['属性值1'] = ''
            item['sx名1'] = ''
            item['sx名2'] = ''

            sizelis = []
            cololist = []
            variationAttributes = detailData['variationAttributes']
            if variationAttributes:
                for variationAttribute in variationAttributes:
                    if variationAttribute['attributeId']=='size':
                        sizelist =variationAttribute['values']
                        for sizer in sizelist:
                            sizelis.append(sizer['id'])
                        item['sx名1'] = 'size'
                    if variationAttribute['attributeId']=='color':
                        colorlist = variationAttribute['values']
                        for color in colorlist:
                            cololist.append(color['id'])
                        item['sx名2'] = 'color'
            arrs = []
            item['面包屑1'] = mianbaoxue
            if sizelis:
                item['sx值1'] = '>'.join(sizelis)
                arrs.append('size#'+'>'.join(sizelis))
            else:
                item['sx值1'] = ''
            if cololist:
                item['sx值2'] = '>'.join(cololist)
                arrs.append('color#'+'>'.join(cololist))
            else:
                item['sx值2'] = ''
            
            item['sx名3'] = ''
            item['sx值3'] = ''
            item['sx名4'] = ''
            item['sx值4'] = ''
            item['属性值1'] = '\n'.join(arrs)
            item['描述1'] = ''
            item['描述2'] = ''
            item['PageUrl'] = data['url']

            results.append(item)
            if len(results)==1000:
                self.sqlite.insermany(results,table)
                results = []
        self.sqlite.insermany(results,table)
        self.sqlite.insermany(down_results,table_down)

    def download(self,dowurls):
        url = dowurls[0]
        name = dowurls[1]
        for i in range(5):
            # time.sleep(5)
            req = requests.get(url,headers=headers_find,timeout=10)
            if req.status_code==200:
                imgend = name.split('/')[-1]
                imgdir = name.replace(imgend,'')
                if not os.path.exists(imgdir):
                    os.makedirs(imgdir)
                with open(name,'wb') as f:
                    f.write(req.content)
                break
            else:
                print(f"下载失败，第{i}次尝试")
                continue

    def saveImg(self):
        down_no = 0
        no = 0
        dowurls = []
        datas = self.collection_find.find().to_list()
        for data in datas:
            no += 1
            detailData = data['products'][data['pid']]['availProduct']
            imgeitem = detailData.get('images')
            if imgeitem:
                for itemk in imgeitem.keys():
                    imgs = imgeitem[itemk]
                    if imgs:
                        down_no += 1
                        imgurl = imgs[0]['url']
                        saveurl = f"{img}{imgname}{no}.jpg"
                        dowurls.append([imgurl,saveurl])
                        break
        
        #单线程
        # for dowurl in dowurls:
        #     self.download(dowurl)

        #多线程
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(self.download,dowurls)

    def main(self):
        ym = int(input('请输入要执行的操作：\n1. 爬取网页\n2. 解析网页找到详情原始数据\n3. 保存最终数据\n4. 保存图片到本地\n请选择下标:'))
        if ym==1:
            self.start()
        elif ym==2:
            self.paser()
        elif ym==3:
            self.save()
        elif ym==4:
            self.saveImg()
        else:
            print('请输入正确的操作')
            return
        print('已完成')

if __name__ == "__main__":
    indexer = indexer()
    indexer.main()
