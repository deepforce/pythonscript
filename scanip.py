# coding=utf_8

import requests
import threading
import Levenshtein
import re

def scan(original_r,cip,ip_begin,original_match,header):
	ip=cip+str(ip_begin)
	try:
		r=requests.get('http://'+ip,headers=header,timeout=1)
	except Exception:
		pass
	else:
		if(r.status_code==original_r.status_code):
			if r.content==original_r.content:
				print('---everything is match!---\n'+ip+'\n--------------------------\n\n\n')
			else:
				if Levenshtein.ratio(r.text,original_r.text)>0.8:
					match=re.search(b"<title>(.*?)</title>",r.content)
					try:
						if match==original_match or match.group()==original_match.group():
							print('--matches>0.8-same title--\n'+ip+'\n--------------------------\n\n\n')
						else:
							print('--matches>0.8-diff title--\n'+ip+'\n--------------------------\n\n\n')
					except Exception:
						if  match==None:
							#扫描网页无标题
							print('-matches>0.8-none title-s-\n'+ip+'\n--------------------------\n\n\n')
						else:
							#原始网页无标题
							print('-matches>0.8-none title-o-\n'+ip+'\n--------------------------\n\n\n')

def loop(original_r,cip,original_match,header):
	global ip_begin,ip_end,mutex
	while 1:
		mutex.acquire()
		if ip_begin > ip_end:
			mutex.release()
			break
		ip=ip_begin
		ip_begin += 1
		mutex.release()
		scan(original_r,cip,ip,original_match,header)

def start():
	global ip_begin,ip_end,mutex
	
	ip_begin=1
	ip_end=254
	mutex=threading.Lock()
	
	cip='180.97.33.'
	address='www.baidu.com'
	
	#cip='220.181.136.'
	#address='www.219.me'
	
	header={"host":address,"Accept-Encoding":"identity","User=Agent":""}
	r=requests.get('http://'+address,headers=header)
	original_match=re.search(b"<title>(.*?)</title>",r.content)
	
	threads=[]
	for i in range(254):
		threads.append(threading.Thread(target=loop,args=(r,cip,original_match,header)))
	for t in threads:
		t.start()

if __name__ == '__main__':
	start()