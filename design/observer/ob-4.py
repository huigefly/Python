import time
import _thread

FOREVER=99999999

class bar_base:
    effect = 'base effect'
    value = 0
    def set(self, value):
        self.value = value
    
    def run(self):
        def progress(_class):
            for i in range(FOREVER):
                # if is_visiable() ....
                print("bar[%s] get: %d" % (
                    _class.effect, 
                    _class.value))
                time.sleep(1)
        # ...
        _thread.start_new_thread(progress, (self, ))
        # ...

class magic_bar(bar_base):
    def __init__(self):
        self.effect = "magic"

class low_bar(bar_base):
    def __init__(self):
        self.effect = "low"

class win_main:
    bar = magic_bar()
    def work(self):
        #....
        self.bar.run()
        #....
    
class win_top:
    bar = low_bar()
    def work(self):
        #....
        self.bar.run()
        #....

class subjec:
    objs = []
    def add(self, obj):
        self.objs.append(obj)
    
    def remove(self, obj):
        self.objs.remove(obj)

    def notify(self, value):
        for obj in self.objs:
            obj.set(value)

class download_base(subjec):
    value = 0
    info = "download base"
    #....
    def init(self):
        pass

    def run(self):
        # ....
        for i in range(20):
            print("----%s progress: %d" % (self.info, i))
            self.notify(i)
            time.sleep(1)
    # ....

class http_download(download_base):
    def init(self):
        self.info = 'http download'

    def run(self):
        super().run()
        print('------------------- http download is ok!!!!!!--------')

class bt_download(download_base):
    def init(self):
        self.info = 'bt download'

class download_factory:
    # input: 1,config; 2, other module, 3...
    def get(self, value):
        if value == 'http':
            return http_download()
        elif value == 'bt':
            return bt_download()


if __name__ == "__main__":
    # create window
    w_main = win_main()
    w_main.work()
    w_top = win_top()
    w_top.work()

    # get download tool
    dl = download_factory().get('http')
    dl.init()

    dl.add(w_main.bar)
    dl.add(w_top.bar)
    
    dl.run()

    time.sleep(2)