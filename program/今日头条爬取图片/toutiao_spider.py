#coding:utf-8
from urllib import urlencode 
# from urllib.parse import urlencode 
import requests
from requests.exceptions import ConnectionError
import os
import re
import json
import pymongo
from hashlib import md5
from multiprocessing import Pool
from config import *
from bs4 import BeautifulSoup
#将捕获json值转化异常改为通用模式
try:
	from json.decoder import JSONDecodeError
except ImportError:
	JSONDecodeError = ValueError

client = pymongo.MongoClient(MONGO_URL,content=False)
db = client[MONGO_DB]

def get_page_index(offset,keyword):
	data = {
		'autoload':'true',
		'count':20,
		'cur_tab':3,
		'format':'json',
		'keyword':keyword,
		'offset':offset,
	}
	params = urlencode(data)
	base = r'http://www.toutiao.com/search_content/'
	url = base +'?' + params
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None

	except ConnectionError :
		print('Connet Error')
		return None

def parse_page_index(text):
	try:
		data = json.loads(text)
		#判断data存在
		if data and 'data' in data.keys():
			for item in data.get('data'):
				yield item.get('article_url')
	#py3的捕获方式
	# except json.decoder.JSONDecodeError:
	#py2的捕获方式
	# except ValueError:
	# 通用的方式
	except JSONDecodeError:
		pass



def get_page_detail(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			print(response.text)
			return response.text
		return None
	except ConnectionError :
		print('Connet Error')
		return None

def save_image(content):
	#os.getcwd()返回当前进程的工作目录
	#md5编码 避免保存重复
	file_path = '{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
	print(file_path)
	#不存在该文件则创建
	if not os.path.exists(file_path):
		with open('file_path','wb') as f:
			f.write(content)
			f.close()

def download_image(url):
    print('Downloading', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except ConnectionError:
        return None

def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('title')
    title = result[0].get_text() if result else ''
    images_pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)
    result = re.search(images_pattern, html)
    if result:
        data = json.loads(result.group(1).replace('\\', ''))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images: download_image(image)
            return {
                'title': title,
                'url': url,
                'images': images
            }


def save_to_mongo(result):
	if db[MONGO_TABLE].insert(result):
		print('Successfully Saved to Mongo', result)
		return True
	return False

def main():
	text = get_page_index(offset,KEYWORD)
	urls = parse_page_index(text)
	for url in urls:
		url = url.replace('group/','a')
		# print(url)
		html = get_page_detail(url)
        result = parse_page_detail(html, url)
        print(result)
        if result: save_to_mongo(result)
	
if __name__ == '__main__':
	# main()
	pool = Pool()
	groups = ([x * 20 for x in range(GROUP_START,GROUP_END+1)])
	pool.map(main,groups)
	pool.close()
	pool.join()