import _thread
import time


def show(threadName):
    cnt = 0
    while cnt < 10:
        time.sleep(1)
        print(threadName)
        cnt += 1


_thread.start_new_thread(show, ('Thread_1',))
_thread.start_new_thread(show, ('Thread_2',))

class a:
    def __init__(self, a1):
        print(a1)
class b:
    def __init__(self, b1):
        print(b1)
class c(a, b):
    def __init__(self):
        pass



