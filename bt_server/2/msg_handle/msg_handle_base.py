class Singleton(type):
    def __init__(self, name, bases, class_dict):
        print ('Singleton init')
        super(Singleton, self).__init__(name, bases, class_dict)
        print ('Singleton init end')
        self._instance = None
    def __call__(self, *args, **kwargs):
        print ('Singleton call')
        if self._instance is None:
            print ('Singleton call just once')
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
            print ('Singleton call just once end')
        return self._instance

class MsgHandleBase:
    __metaclass__ = Singleton
    def init(self, data):
        self.data = data

    def run(self):
        print("i am wroking")
        pass

    def response(self):
        print("i response you")
        pass
