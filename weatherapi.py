#encoding=utf-8
import sys, urllib.parse, urllib.request, json

appkey = 'cd505742eb5d1599b64aff9050f703fc' #您申请到的数据的APPKEY
url = 'http://v.juhe.cn/weather/index?cityname=%E5%B9%BF%E5%B7%9E' #数据API请求URL
paramsData = {'key': appkey} #需要传递的参数
params = urllib.parse.urlencode(paramsData).encode(encoding='UTF8')

req = urllib.request.Request(url, params)
req.add_header('Content-Type', "application/x-www-form-urlencoded")
resp = urllib.request.urlopen(req)
content = resp.read().decode()
if(content):
    result = json.loads(content, 'utf-8')
    error_code = result['error_code']
    if(error_code == 0):
        data = result['result'] #接口返回结果数据
        print(data)
    else:
        errorinfo = str(error_code)+":"+result['reason'] #返回不成功，错误码:原因
        print(errorinfo)