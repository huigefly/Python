
from test import CTest
import coverage

# cov=coverage.coverage(data_file=".coverage", data_suffix=True)
# cov.start()

class CMain(object):

    def __init__(self, index):
        self.index = index

    def test1(self):
        print("helloworld test1")

    def test2(self):
        print("helloworld test2")

    def test3(self):
        print("helloworld test3")

    def test4(self):
        print("helloworld test4")

    def test5(self):
        self.test1()
        self.test2()
        if self.index == 99:
            self.test3()
        self.test4()

# cov.stop()
# cov.save()

if __name__ == "__main__":
    m = CMain(199)
    m.test5()

    t = CTest(99)
    t.test5()