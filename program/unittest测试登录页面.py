# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import unittest
class Interface(unittest.TestCase):
    """classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，
        可以来调用类的属性，类的方法，实例化对象等。"""
    @classmethod
    def setUpClass(cls):
        req = requests.post(url = 'url',
                            date = {'loginName':'admin', 'psaaWord':'123456'})
        
        global cookie
        cookie = req.cookies.get_dict()  #获取cookie

    @classmethod
    def tearDownClass(cls):
        pass

    def test_login(self):
        u'登录平台接口'
        req = requests.post(ur = 'url',
                            date = {'loginName':'admin', 'psaaWord':'123456'})
        dicts = json.loads(req.content) #json.loads:用于解码Json,json.dumps : 用于编码json  json在传输的时候就是字符串
        try:
            self.asserEqual(dicts['msg'], u'登录成功！', 'status:200')
        except AssertionError as e:
            print e
        else:
            results = req.json()
            #因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
            print json.dumps(results,encoding = 'UTF-8', ensure_ascii=Flase) 

    def test_get_mine(self):
        u'访问我的页面'
        #可通过调用setUpClass来获取cookies并post requests一个页面