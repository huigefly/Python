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

class bt:

    bar_list = []

    def add(self, bar):
        self.bar_list.append(bar)

    def remove(self, bar):
        self.bar_list.remove(bar)

    def notify(self, value):
        for bar in self.bar_list:
            bar.set(value)

    def run(self):
        # ....
        for i in range(20):
            print("----bt progress: %d" % i)
            time.sleep(1)

            # self.bar.set(i)
            self.notify(i)
        # ....

if __name__ == "__main__":
    w_main = win_main()
    w_main.work()

    w_top = win_top()
    w_top.work()

    bt = bt()
    bt.add(w_main.bar)
    bt.add(w_top.bar)
    bt.run()

    time.sleep(2)