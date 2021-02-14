import urllib.request
import urllib.parse


url = "http://www.baidu.com/"
#发起一个request请求,得到返回对象
res = urllib.request.urlopen(url)
#查看http访问状态
if res.status == 200:
    print("访问成功")
    #获取数据
    data = res.read().decode("utf-8")
    print(data)