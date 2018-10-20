#coding:utf-8
import requests
import json


#Simple One:适用于cookie不会变化的情况
params = json.dumps({'user_id': '100100010050', \
						'password': '123123', \
						'kaptcha': '7777'}) #编码Json格式
header = {'Content-Type': 'application/json', 'Connection': 'keep-alive', 'platForm': 'baike'}
r = requests.post(url=r"http://XXX.XX.com.cn/server/ws/pub/token/access_token/tradeUser",headers=header, data=params)
if (r.status_code >= 200 and r.status_code < 300):
    print "登录成功"
else:
    print "无法登录"
print "Cookie is set to:"
print r.cookies.get_dict()
print "-----------------"
print "Going to profile page..."
print r.text

#Complex One:适用于cookie可能会被修改的情况下，使用request.Session
s = requests.session()
params = json.dumps({'user_id': '100100010050', \
						'password': '123123', \
						'kaptcha': '7777'}) #编码Json格式
header = {'Content-Type': 'application/json', 'Connection': 'keep-alive', 'platForm': 'baike'}
r = s.post(url=r"http://XXX.XX.com.cn/server/ws/pub/token/access_token/tradeUser",headers=header, data=params)
if (r.status_code >= 200 and r.status_code < 300):
    print "登录成功"
else:
    print "无法登录"
print "Cookie is set to:"
print r.cookies.get_dict()
print "-----------------"
print "Going to profile page..."
print r.text

"""在requests库中可以定制会话级别的cookies，
	以保证整个通信过程中都可以使用到cookies"""

#增加
s = requests.session()
s.cookies.set('mycookie','value')  #设置会话cookies
r = s.get("http://www.baidu.com")
print s.cookies.get_dict()	#输出cookie

#更新
s = requests.session()
s.get('http://www.baidu.com')
print s.cookies.get_dict()	#更新前
c = requests.cookies.RequestsCookieJar()	#定义一个cookie对象
c.set('cookie-name', 'cookie-value')	#新增cookie的值
print s.cookies.get_dict()	#更新后

#全部删除
s = requests.session()
s.get('http://www.baidu.com')
print s.cookies.get_dict()	#删除前
s.cookies.clear()	#删除cookies，也可以使用s.cookies = None的方式将所有的cookies删除
print s.cookies.get_dict()	#删除后

#指定键删除（巧妙使用None删除指定键）
s = requests.session()
try:
	s.get('http://www.baidu.com')
	print s.cookies.get_dict()	#删除前
	s.cookies.set('BDORZ',None)	#删除cookies中BDORZ的值
	print s.cookies.get_dict()	#删除后
except Exception,e:
	print e