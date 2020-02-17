import copy


class A:

    def __init__(self):
        self.x = 18
        self.msg = 'Hello'


class B(A):

    def __init__(self):
        A.__init__(self)
        self.y = 34

    # format class string when print
    def __str__(self):
        return '{}, {}, {}'.format(self.x, self.msg, self.y)

if __name__ == '__main__':
    b = B()
    c = copy.deepcopy(b)
    # c = copy.copy(b)
    # print b.__dict__
    # print B.__dict__
    for i in (b, c):
        print i
    print([str(i) for i in (b, c)])
    print([i for i in (b, c)])
