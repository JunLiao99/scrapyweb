from django.db import models
from django.db import connection

import requests
import pyquery
from . db_connection_string import dbConfig
import pymysql as pmsql
import codecs
import time
import os
# Create your models here.
class bookingq:
    def news(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM work_go.intime_news")
            datas = cursor.fetchall()
        return datas
    
    def all(self):
        with connection.cursor() as cursor:
            cursor.execute("Select * from intime_news")
            data5 = cursor.fetchone()
        return data5

    # 抓取單筆新聞
    # def grabPage(fhref,txt1,i):
    #     # 判斷連結是否有效
    #     if fhref is None:
    #         return
    #     print("詳細頁面-------------------------------------------------------------------------")
    #     # 下載

    #     response = requests.get(fhref)
    #     time.sleep(3)
    #     # print(response)
    #     # 判斷 HTTP 回傳代碼是 200 OK
    #     if response.status_code == 200:
    #         # 開啟 UTF-8 編碼的文字檔
    #         f = codecs.open('nda_det.txt', 'w', encoding='utf-8')
    #         f.write(response.text)
    #         f.close()


    #         # 將下載回來的原始碼轉成 PyQuery 的文件實體
    #         e = pyquery.PyQuery(response.text)
    #         # 讀取店家資料      
    #         # print(e)
    #         dt = e('div#story_body_content>span>p').text()
    #         dtc = (dt.split(' ', 1 ))
    #         print(dtc[1])
    #         print(txt1)
    #         print(fhref)
    #         excute_sql("insert into work_go.intime_news (Title,news,http) values(%s, %s, %s)", txt1,dtc[1],fhref)

            
            
    def gooo(self):
        num = 1
        i = 50060
        # while True:
        responseS = "https://nba.udn.com/nba/index?gr=www"
        response = requests.get(responseS)
        time.sleep(5)
        # 判斷 HTTP 回傳代碼是 200 OK
        if response.status_code == 200:
            # 開啟 UTF-8 編碼的文字檔
            f = codecs.open('nba.txt', 'w', encoding='utf-8')
            f.write(response.text)
            f.close()

            d = pyquery.PyQuery(response.text)
            # print(d)
            posts = d('div#mainbar>div#news>#news_body>dl>dt')
            for post in posts.items():
                # print(post)
                txt1 = post('h3').text()
                # print("####################################""""start""""######################################")
                href = post('a').attr('href')
                if href is None:
                    return
                fhref = "https://nba.udn.com" + href
                # grabPage(fhref,txt1,i)

                if fhref is None:
                    return
                print("詳細頁面-------------------------------------------------------------------------")

                response = requests.get(fhref)
                time.sleep(3)
                # print(response)
                # 判斷 HTTP 回傳代碼是 200 OK
                if response.status_code == 200:
                    # 開啟 UTF-8 編碼的文字檔
                    f = codecs.open('nda_det.txt', 'w', encoding='utf-8')
                    f.write(response.text)
                    f.close()


                    # 將下載回來的原始碼轉成 PyQuery 的文件實體
                    e = pyquery.PyQuery(response.text)
                    # 讀取店家資料      
                    # print(e)
                    dt = e('div#story_body_content>span>p').text()
                    dtc = (dt.split(' ', 1 ))
                    # print(dtc[1])
                    print(txt1)
                    # print(fhref)

                    ####

                    with connection.cursor() as cursor:
                        cursor.execute("select Title from intime_news")
                        data = cursor.fetchone()
                        if data != None:
                            print("QQQQQQQQQQQQQQ",data,"QQQQQQQQQQQQ")
                    
                    if data == None:
                        with connection.cursor() as cursor:
                            sql = """insert into intime_news(Title,news,http)
                                values(%s,%s,%s)"""
                            cursor.execute(sql,(txt1,dtc[1],fhref))
                    elif data != None:
                        if data[0] != txt1:
                            with connection.cursor() as cursor:
                                sql = """insert into intime_news(Title,news,http)
                                        values(%s,%s,%s)"""
                                try: 
                                    cursor.execute(sql,(txt1,dtc[1],fhref))
                                except:
                                    connection.rollback()
                    time.sleep(1)  # 自定义延时  
                    i = i+1
        else:
            print('搜尋結果回傳代碼並非 200')
        num += 1