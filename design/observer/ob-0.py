import time
import _thread

class win_main:
    value = 0

    def set(self, value):
        self.value = value

    def update(self, value):
        print("win_main get: %d" % value)

    def run(self):
        def progress(_class):
            for i in range(9999999999999):
                print("win main is running......")
                #if is_visible & value change
                self.update(_class.value)
                time.sleep(1)
        # ...
        _thread.start_new_thread(progress, (self, ))
        # ...

class bt:

    def __init__(self):
        self.win = win_main()
        self.win.run()

    def run(self):
        # ....
        for i in range(20):
            print(" bt progress: %d" % i)
            self.win.set(i)
            time.sleep(1)
        # ....

if __name__ == "__main__":
    bt().run()

    time.sleep(2)