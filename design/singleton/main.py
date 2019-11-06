def singleton(cls, *args, **kwargs):
    instances = None
    def get_instance(*args, **kwargs):
        nonlocal instances
        if instances is None:
            print ("singleton is None")
            instances = cls(*args, **kwargs)
        return instances
    return get_instance

@singleton
class Bar(object):
    def __init__(self,name):
        self.name = name

if __name__ == '__main__':
    b1 = Bar('alex')
    b2 = Bar('hello')
    print(b1.name)
    print(b2.name)