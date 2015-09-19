#coding=utf-8
'''模块'''
import urllib.request
import re

'''抓取整个页面'''
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

'''抓取图片并保存'''
def getImg(html): # 正则匹配
	html = html.decode('utf-8')
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		urllib.request.urlretrieve(imgurl,'F:\local\%s.jpg' % x)# 第二个参数表示保存路径
		x+=1

'''抓取指定网页'''
html = getHtml("http://tieba.baidu.com/p/3735966740")

getImg(html)