class base(object):
    def work(self):
        pass
    def talk(self):
        pass

class sale(base):
    def work(self):
        print ("sale work")
    def talk(self):
        print ("sale talk")

class proxy(base):
    def __init__(self):
        self.realWork = sale()

    def work(self):
        print ("here proxy call real worker!")
        self.realWork.work()

if __name__ == '__main__':
    print ("helloworld")
    p = proxy()
    p.work();