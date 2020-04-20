import time
import _thread

class win_main:
    value = 0

    def set(self, value):
        self.value = value
        #if is_visible
        self.update(value)

    def update(self, value):
        print("win_main get: %d" % value)

class win_top:
    value = 0

    def set(self, value):
        self.value = value
        #if is_visible
        self.update(value)

    def update(self, value):
        print("win_top get: %d" % value)

class bt:

    win_list = []

    def add(self, win):
        self.win_list.append(win)

    def remove(self, win):
        self.win_list.remove(win)

    def notify(self, value):
        for win in self.win_list:
            win.set(value)

    def run(self):
        # ....
        for i in range(20):
            print("----bt progress: %d" % i)

            # self.win.set(i)
            self.notify(i)

            time.sleep(1)
        # ....

if __name__ == "__main__":
    w_main = win_main()
    w_main.run()

    w_top = win_top()
    w_top.run()

    bt = bt()
    bt.add(w_main)
    bt.add(w_top)
    bt.run()

    time.sleep(2)