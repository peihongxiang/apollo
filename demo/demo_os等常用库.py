# import os
# os.mkdir('hello')
# print(os.listdir("./"))
# os.removedirs('hello')
# print(os.getcwd())
# print(os.path.exists('b'))
# os.mkdir('b')
# if not os.path.exists('b'):
#     os.mkdir('b')
# if not os.path.exists('b.txt'):
#     with open ('b/testb.txt','w') as f:
#         f.write("hello os using")

# import time
# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H-%M-%S',time.localtime()))

#获取两天前得时间
# now_timestamp = time.time()
# two_day_before = now_timestamp - 60*60*24*2
# print(time.strftime('%Y:%m:%d %H:%M:%S',time.localtime(two_day_before)))

# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.status)
# print(response.read())
# print(response.headers)

import math
print(math.ceil(3.5))#大于该数的最小整数
print(math.floor(4.5))#小于该数的最大整数
print(math.sqrt(4))#求平方根



