
from functools import wraps

"""
简单得装饰器
"""
# def mydecorator(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print('before')
#         print(a_func())
#         print('after')
#     return wrapTheFunction
#
# @mydecorator
# def my_method():
#     s = "hello world"
#     return s
# print(my_method.__name__)
# my_method()

"""
装饰器的应用
"""
def decorator_name(a_func):
    @wraps(a_func)
    def wrapTheFunction(*args,**kwargs):
        if not can_run:
            return "Function will not run"
        return a_func(*args,**kwargs)
    return wrapTheFunction

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())

can_run = False
print(func())

"""
Authorization
"""
# def decorator_authorization(a_func):
#     @wraps(a_func)
#     def wrapTheFunction(*args,**kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username,auth.password):
#             authenticate()
#         return f(*args,**kwargs)
#     return wrapTheFunction

"""
log
"""

def logit(a_func):
    @wraps(a_func)
    def wrappp(*args,**kwargs):
        print(a_func.__name__ + " is called")
        return a_func(*args,**kwargs)
    return wrappp
@logit
def main_func(x):
    return x + x

result = main_func(5)
print(result)
from functools import wraps

"""带参数的装饰器"""

def login(logfile='out.log'):
    def log_decorator(func):
        @wraps(func)
        def wrappp(*args,**kwargs):
            log_string = func.__name__ +" is called"
            with open(logfile,'a') as opened_file:
                opened_file.write(log_string)
            return func(*args,**kwargs)
        return wrappp
    return log_decorator

@login()
def myfunc1():
    pass
myfunc1()

"""
装饰器类
"""

class logit1(object):
    def __init__(self,log_file='hello.log'):
        self.log_file = log_file

    def __call__(self,func):
        @wraps(func)
        def wrappp(*args,**kwargs):
            log_string = func.__name__+" is called"
            # with open(self.log_file,'a') as f:
            #     f.write(log_string)
            self.write(self.log_file,log_string)
            return func(*args,**kwargs)
        return wrappp
    def write(self,file,content):
        with open(file,'a') as f:
            f.write(content+'\n')
@logit1()
def my_main():
    return "hi nihao"

my_main()