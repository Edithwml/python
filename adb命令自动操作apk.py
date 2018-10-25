#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年9月3日
@author: Cowumiaoling
手机自动从网页下载最新包并安装
'''
import os
import re
import requests

#os.system('adb devices')  # os.system是不支持读取操作的 os.popen支持读取


def packageList():
    packages_str = os.popen('adb shell "pm list packages | grep com.gf"').read()
    print("已安装的包列表如下：\n")
    # strip用于去掉字符串前后的空格、回车等空白字符
    # replace方法可以替换字符串，这里把所有"package:"替换成""，等同于去掉
    # split方法用于分割字符串，按照换行符来分割就能得到一个包含所有com.gf包名的list了
    GF_apk = packages_str.strip().replace("package:", "").split("\n")
    print(GF_apk)
    # 输入要卸载的包名0或1
    i = int(input("输入数字选择要操作的包，从0开始计算：\n"))
    # 输入的数字大于列表最大的长度或者小于0都认为是不存在
    if i > len(GF_apk) - 1 or i < 0:
        print("该包不存在")
    else:
        return GF_apk[i]
# 卸载apk
def uninstall():
    u = packageList()
    status = os.popen("adb uninstall " + u).read()
    print(status)
    print("uninstall %s " % u + status)
#清除缓存
def ClearCache():
    c = packageList()
    status = os.popen("adb shell pm clear "+c).read()
    print(status)
    print("clearCache %s "%c + status)

# 从网页下载最新的apk并安装
def install():
    # 因为需要定义爬取的规则，所以不能随便就都支持，这里就先支持两个包好了
    packages = ["client", "clickeggs","clickeggs_Daily"]
    i = int(input("请输入你要安装的包序号：\n0. client\n1. clickeggs\n2. clickeggs_Daily"))
    if i > len(packages) - 1 or i < 0:
        print("不支持的包")
    else:
        # 下载包
        apk = download(packages[i])
        # 包下载成功的话就执行安装了
        if apk != None:
            # 加上-r可以覆盖安装
            status = os.popen("adb install -r " + apk).read()
            #这里实际没有打印出来
            print(status)
            print("install " + packages[i] + status)

# 截取屏幕并保存
def screen_cap():
    os.system("adb shell screencap /sdcard/sc.png")
    os.system("adb pull /sdcard/sc.png D:\pic") #保存到电脑
    print("图片保存成功")

# 录制视频并保存
def screen_record():
    pass

# 重启手机
def reboot():
    os.system("adb reboot")


# 连接设备，连接成功时返回False，否则返回True，结果while就可以在连接失败的时候一直重试了
def connect():
    # 补充：没有连接设备时，尝试进行自动连接。
    # 但设备的ip地址通常都是变化的，所以应该让输入会更灵活，不用每次都改代码 ~
    # 2.7版本是要用raw_input
    ip_port = raw_input("没有任何设备已连接，请先开启usb调试，再输入你要连接的设备[ip地址]，端口默认为5555, ip地址默认为10.2.236.239\n")
    # 如果没有输入任何东西，默认把ip设置为192.168.1.100
    if ip_port.strip() == '':
        ip_port = "10.2.236.239"

    # 连接
    connect = os.popen("adb connect " + ip_port).read()
    print(connect)
    # 分析adb connect的返回值，发现有"connected"时就是成功了
    
    i = connect.find("connected")
    j = connect.find("unable")
    if i != -1:
        print("设备连接成功")
        return False
    # elif j.find("unable"):
    #     print("请打开手机的开发者模式")
    else:
        return True

def download(package):
    # 先分析网页，然后定义一套规则，job指该包的任务，regex指搜索该包下载地址的正则表达式
    #(.*?)是非贪婪,(.*)是贪婪匹配
    d = {
        "client": {
            "job": "GF_Mobile_Android_Debug",
            "regex": "lastSuccessfulBuild/artifact/gf_client_android/build/outputs/apk(.*?).apk"
        },
        "clickeggs": {
            "job": "Android_Clickeggs_Debug",
            "regex": "lastSuccessfulBuild/artifact/ci/output/(.*?).apk"
        },
        "clickeggs_Daily": {
            "job": "Clickeggs_Branch_Daily",
            "regex": "lastSuccessfulBuild/artifact/ci/output/(.*?).apk"
        }
    }
    # package传进来的就是client或clickeggs了，如果在规则里面没定义就提示不支持
    if d[package] == None:
        print("不支持的包")
        return
    # 拼接出要下载的包需要爬取的网页地址
    view = "http://这里是地址/" + d[package]["job"] + "/"
    # 获取网页内容
    c = requests.get(view).content
    apkUrl = ''
    # 在网页里面按照规则匹配出最新包的地址 re.search 扫描整个字符串并返回第一个成功的匹配
    search = re.search(d[package]["regex"], str(c))
    # 如果有匹配到
    if search != None:
        # 拼接下载地址
        #正则group取第一条 groups取所有
        apkUrl = view + search.group()
    if apkUrl == '':
        print("未找到包")
        return
    else:
        # 下载该apk
        res = requests.get(apkUrl)
        #下载文件并保存
        #用as code写不用在写close语句
        with open("tmp.apk", "wb") as code:
            code.write(res.content)
        print("下载最新包成功")
        return "tmp.apk"

def main():
    # 查看设备是否连接
    devices = os.popen("adb devices").read()  # popen支持读取操作
    print(devices)
    # 应当根据str判断超过两个devices为真
    # 补充：因为不管有没有设备连接，都总是会打印"List of devices attached"这句话的
    # 这句话已经包含了一个"device"。
    # 如果有其它设备连接的话， 则会打印类似于"2affa89a	device"的结果，也就是说每连接一个设备会多一个"device"
    # 所以，device只有一个时, 可以证明没有连接到任何设备
    if devices.count("device") == 1:
        # 如果返回True就一直重试
        while connect():
            print("设备连接失败")
    else:
        print("设备连接成功")
    # 通过获取输入的值，比如1，调用不同的方法
    while True:
        b= int(input("\n请输入序号选择要执行的操作：\n1. install\n2. uninstall\n3. reboot\n4. screen_cap\n5. ClearCache\n6. screen_record"))
        if b == 1:
            install()
        elif b == 2:
            uninstall()
        elif b == 3:
            reboot()
        elif b == 4:
            screen_cap()
        elif b == 5:
            ClearCache()
        elif b == 6:
            screen_record()



if __name__ == "__main__":
    main()
