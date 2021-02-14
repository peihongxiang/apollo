import time
import threading

class myThread (threading.Thread):
    def __init__(self,id,name,stime):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.stime = stime

    def run(self):
        print("开始线程：" +self.name)
        threadLock.acquire()
        print_time(self.name,self.stime,3)
        threadLock.release()
        print("结束线程：" +self.name)
threadLock = threading.Lock()
threads = []
def print_time(name,delay,counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (name, time.ctime(time.time())))
        counter -=1

first_thread = myThread(1,"thread1",1)
second_thread = myThread(2,"thread2",2)

first_thread.start()
second_thread.start()

threads.append(first_thread)
threads.append(second_thread)
for t in threads:
    t.join()
# first_thread.join()
# second_thread.join()
print("退出主线程")

