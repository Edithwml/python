#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import csv
import sys
reload(sys)
sys.setdefaultencoding("utf8")
#网易云音乐榜的第一页
url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'
driver = webdriver.PhantomJS()

#准备好储存歌单的csv文件
csv_file = open("playlist.csv","wb")
writer = csv.writer(csv_file)
writer.writerow(['标题','播放数','链接'])

#解析每一页知道’下一页‘为空
while url != 'javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame("contentFrame")
    #定位歌单标签
    data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    #解析一页中的所有歌单
    for i in range(len(data)):
        #获取播放数
        nb = data[i].find_element_by_class_name("nb").text
        if '万' in nb and int(nb.split("万")[0]>200):
            #获取播放数大于200万的歌单封面
            msk = data[i].find_element_by_css_selector("a.msk")
            #把封面上的标题和链接连同播放数下载下来
            writer.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])
    #定位下一页的url
    url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
csv_file.close()