import requests
import sqlite3
import json


class Proxy_sqlite:
    def __init__(self):
        self.conn=sqlite3.connect('proxy_from_XMX.db')
        self.cursor=self.conn.cursor()

    def insert(self,proxy):
        insert_sql_word='INSERT INTO proxy_from_XMX (proxy) VALUES ("%s")'%(proxy)
        self.cursor.execute(insert_sql_word)
        self.conn.commit()

    def create_table(self):
        create_table_word='CREATE TABLE proxy_from_XMX (proxy char(50))'
        self.cursor.execute(create_table_word)
        self.conn.commit()

    def select(self):
        select_table_word='SELECT * FROM proxy_from_XMX'
        result=self.cursor.execute(select_table_word)
        self.conn.commit()
        return result.fetchall()

    def delete_all(self):
        delete_all_info_word='DELETE FROM proxy_from_XMX'
        self.cursor.execute(delete_all_info_word)
        self.conn.commit()

    def update_all_info(self,proxy_list):
        self.delete_all()
        for one_proxy in proxy_list:
            self.insert(proxy=one_proxy)



    def close(self):
        self.conn.close()

def get_proxy():
    session1=requests.session()
    response1=session1.request(method='get',url='http://192.168.8.52:8899/')



if __name__ == '__main__':
    proxy_class=Proxy_sqlite()
    # proxy_class.create_table()
    # proxy_class.insert(proxy='192.168.0.4:8080')
    for i in  proxy_class.select():
        print i[0]