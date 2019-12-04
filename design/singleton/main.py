'''
#method 1
def singletonfunc(cls, *args, **kwargs):
    #print ("singleton enter")
    instances = None  #call once
    def get_instance(*args, **kwargs):
        #print ('singleton getinstance')
        nonlocal instances #py3 ok, py2 no
        if instances is None:
            #print ("singleton is None")
            instances = cls(*args, **kwargs)
        return instances
    return get_instance

@singletonfunc
class Bar(object):
    def __init__(self,name):
        print ('bar init:', name)
        self.name = name
'''
#method 1 other way bibao
def singleton(cls):
    instances = {}
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

@singleton
class car(object):
    def __init__(self, name):
        print ('car init:', name)
        self.name = name

# method 2 metaclass
class Singleton(type):
    def __init__(self, name, bases, class_dict):
        print ('Singleton init')
        super(Singleton, self).__init__(name, bases, class_dict)
        self._instance = None
    def __call__(self, *args, **kwargs):
        print ('Singleton call')
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance
    
class base:
    def get(self):
        return 1000

class house(base, metaclass=Singleton): #py3 ok
#class house():
 #   __metaclass__ = Singleton #py2 ok, py3 no
    def __init__(self, name):
        #super(house, self).__init__()        
        print ('house name,', name)
        self.name = name
'''
class newsingleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(newsingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class gf(newsingleton):
    def __init__(self, name):
        print ('gf name:', name)
        self.name = name
'''        

if __name__ == '__main__':
    '''
    b1 = Bar('alex')
    b2 = Bar('hello')
    print(b1.name)
    print(b2.name)
    c1 = car('audi')
    c2 = car('baoma')
    print(c1.name)
    print(c2.name)
    '''
    
    h1 = house('bighouse')
    h2 = house('smallhoust')
    print(h1.name)
    print(h2.name)
    print(h2.get())
    
    '''
    g1 = gf('beutiful')
    g2 = gf('ugly')
    g3 = gf('shenme')
    print(g1.name, id (g1))
    print(g2.name, id (g2))
    print(g3.name, id (g3))
    '''