# coding=utf-8

'''
mongo数据查询
author:cowumiaoling
Created on 2018年11月21日
'''

from pymongo import MongoClient
import re


class MongoOperation:
    def __init__(self):
        self.db = None

    # 连接数据库
    def db_connect(self, uri, db_name):
        try:
            client = MongoClient(uri)
            self.db = client.get_database(db_name)  # 连接数据库
        except:
            raise

    # 获取查询条数
    def get_mongo_count(self, table, f_condition, projection=None):
        test_table = self.db.get_collection(table)
        try:
            num = test_table.find(f_condition, projection).count()
            return num
        except:
            raise

    # 只查询一条记录
    def mongo_find_one(self, table, f_condition, projection=None):
        test_table = self.db.get_collection(table)
        try:
            result = test_table.find_one(f_condition, projection)
            return result
        except:
            raise

    # 查询全部记录
    def mongo_find(self, table, f_condition, projection=None):
        test_table = self.db.get_collection(table)
        f_results = []
        try:
            results = test_table.find(f_condition, projection)
            for document in results:
                f_results.append(document)
            return f_results
        except:
            raise

    # 查询全部记录并排序
    def mongo_find_sort(self, table, f_condition, projection=None):
        test_table = self.db.get_collection(table)
        f_results = []
        sort_condiction = {"_id":"-1"}
        try:
            # results = test_table.find(f_condition, projection).sort({"requests_time":-1})
            # 排序没有用列表会报错TypeError: if no direction is specified, key_or_list must be an instance of list
            results = test_table.find(f_condition, projection).sort([("_id",-1)])
            for document in results:
                f_results.append(document)
            return f_results
        except:
            raise


    def mongo_remove(self, table, f_condition, projection=None):
        test_table = self.db.get_collection(table)
        try:
            test_table.remove(f_condition, projection)
        except:
            raise

    # 获取子分类
    def get_categroy(self, parent_categroy):
        cat_dict = {}
        f_condition = {"name": parent_categroy}
        cats = self.mongo_find_one('CategoryGroup', f_condition)
        for index in cats['categoryList']:
            c_condition = {"_id": index.id}
            cat = self.mongo_find_one('Category', c_condition)
            cat_dict[cat['name']] = index.id

        return cat_dict

    # 字符串去除敏感词
    def get_str_without_sensitive_word(self, orgin_str):
        f_condition = {}
        s_words = self.mongo_find('Sensitive', f_condition)
        final_str = orgin_str
        for s_word in s_words:
            re_str = "0" * len(s_word['word'])
            if re.search(s_word['word'], orgin_str, flags=2):
                final_str = re.sub(s_word['word'], re_str, orgin_str, flags=2)
        return final_str

    #插入问题


    #插入回答
    def insert_answer_cat_15(self,table,insert_dict):
        test_table = self.db.get_collection(table)
        #批量插入
        answers = {}
        try:
            result = test_table.insert_many(insert_dict)
            return result
        except:
            raise
    #新增一条
    def insert_one_answer_cat_15(self,table,insert_dict):
        test_table = self.db.get_collection(table)
        #批量插入
        answers = {}
        try:
            result = test_table.insert_one(insert_dict)
            return result
        except:
            raise
def main():
    #查询订单id
    JYS_Mon = MongoOperation()
    JYS_uri = 'mongodb://XXX'
    JYS_db_name = 'crmii' 
    JYS_Mon.db_connect(JYS_uri, JYS_db_name)
    JYS_table_name = "order"
    JYS_f_condition = {"client_id":"424689-1"}
    JYS_f_result = JYS_Mon.mongo_find_sort(JYS_table_name,JYS_f_condition)
    print JYS_f_result[0]['_id']



if __name__ == '__main__':
    main()
    
    

