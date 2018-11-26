import requests
from requests.exceptions import RequestException
import re
from multiprocessing import Pool

def get_one_page(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			sleep(20)
			return response.text
		return None
	except RequestException:
		print('访问异常')
		return None

def parse_one_page(html):
	#加入re.S会将\n换行符一起匹配
	pattern = re.conpile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
	items = re.findall(pattern,html)
	for item in items:
		yield {
			'index':item[0],
			'image':item[1],
			'title':item[2],
			'actor':item[3].strip()[3:],  #从第三位开始取
			'tiem':item[4].strip()[5:],
			'score':item[5]+item[6]
		}
def write_to_file(content):
	# a 表示若文件存在以插入的形式写入
	# encoding指定写入文件的制定编码
	with open('result.txt','a',encoding='utf-8') as f:
		#json.dumps 将字典转化为字符串
		#json.dumps序列化时对中文默认使用ascii编码，想输出中文需要设定ensure_ascii=False
		f.write(json.dumps(content,ensure_ascii=False) + '\n')
		f.close()


def main(offset):
	url = r'http://maoyan.com/board/4?offset=' + str(offset)
	html = get_one_page(url)
	print(html)
	for item in parse_one_page(html):
		print(item)
		write_to_file(item)

if __name__ == '__main__':
	#1.for循环调用main函数
	for i in range(10):
        main(offset=i * 10)

     #2.使用进程池
     
     #创建进程池
     pool = Pool()
     #第一个参数是函数，第二个参数是一个迭代器，将迭代器中的数字作为参数依次传入参数中
     pool.map(main,[i*10 for i in range(10)])
     #关闭pool，使其不再接受新的（主进程）任务
     pool.close()
     #pool.join() 是说：主进程阻塞后，让子进程继续运行完成，子进程运行完成后，再把主进程全部关掉
     pool.join()
     