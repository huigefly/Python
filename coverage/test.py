import coverage

# cov=coverage.coverage(data_file=".coverage", data_suffix=True)
# cov.start()

class CTest(object):

    def __init__(self, index):
        self.index = index

    def test1(self):
        print("nihao test1")

    def test2(self):
        print("nihao test2")

    def test3(self):
        print("nihao test3")

    def test4(self):
        print("nihao test4")

    def test5(self):
        self.test1()
        self.test2()
        if self.index == 99:
            self.test3()
        self.test4()


if __name__ == "__main__":
    m = CTest(99)
    m.test5()

# cov.stop()
# cov.save()