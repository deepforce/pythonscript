# coding=utf-8

import re

def strings(url):
	list1 = ['.php', '.html', '.asp', '.jsp']
	for lis in list1:
		suffix = re.findall(lis, url)
		if len(suffix) > 0:
			return lis


url = 'http://www.cnblogs.com/fnng/archive/2013/05/20/3089816.html'


a = strings(url)

print(a)