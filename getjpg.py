#coding=utf-8
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
	html = html.decode('utf-8')
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
		x+=1

html = getHtml("http://tieba.baidu.com/p/3735966740")

getImg(html)