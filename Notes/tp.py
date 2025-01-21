from threading import *

class Test:
    def display(self):
        for i in range(10):
            print("child thread",i)
obj = Test()

t= Thread(target=obj.display())
t.start()
for i in range(10):
    print("Main thread start",i)