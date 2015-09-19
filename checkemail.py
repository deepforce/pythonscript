#coding=utf-8
import re

# 验证有效的邮箱格式

'''
[^\._-]         不匹配点、下划线和横杠
[\w\.-]         匹配包括下划线的任何单词字符、点和横杠
[A-Za-z0-9]     匹配大小写字母和数字
[A-Za-z]        匹配大小写字母
(?:[A-Za-z0-9]+\.) 非获取匹配
'''


def emails(e):
	if len(e) >= 5:
		if re.match("[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+", e) != None:
			return '邮箱格式正确！'
	return '邮箱格式有误!'

e = input("请输入email:")
print(e)
a = emails(e)
print(a)