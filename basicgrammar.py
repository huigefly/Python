import os

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-p", "--pdbk", action="store_true",
                  dest="pdcl",
                  default=False,
                  help="write pdbk data to oracle db")
parser.add_option("-z", "--zdbk", action="store_true",
                  dest="zdcl",
                  default=False,
                  help="write zdbk data to oracle db")

(options, args) = parser.parse_args()

if options.pdcl==True:
    print 'pdcl is true'
if options.zdcl==True:
    print 'zdcl is true'


os._exit(0)


def getvalue():
    return 1000;

def equip(cls, basetype, dict):
    if '__doc__' not in dict:
        dict['__doc__'] = getvalue()
    return type (cls, basetype, dict)

# class myclass(metaclass = equip):
#     def alright(self):
#         return 'okay'
#
# ma = myclass()
# print (ma.__class__, ma.__doc__)



os._exit(0)
def method(self):
    return 1
kclass = type('myclass', (object,), {'method': method})
a = kclass()
print (kclass)
print (a)
print (a.method())






print ('--------------- meta program')
class unit(object):
    def __new__(cls):
        print ("unit __new__,", cls.__class__)
        if not hasattr(cls, "_instance"):
            cls._instance = super(unit, cls).__new__(cls)
        return cls._instance
    def __init__(self):
        print ("unit __init__,", self)
    def __call__(self):
        print ("unit __call__")

class cli(unit):
    def __init__(self):
        super(cli, self).__init__()
        print ('cli init')


print ("a")
a = unit()
print ("b")
b = unit()
print ("c")
c = cli()
print ("d")
d = unit()


#变量
print("---value")
value=100
print("value:", value)
print("value:{0}".format(value))


#字符串
print("---buffer test")
buffer="helloworld"
buffer2="nihao shijei"
buffer3=buffer + buffer2
print("size:", buffer.title())
print(buffer3)

#数字
print("---number")
v1=100
v2=99
v3=v1+v2+200
msg="shenme " + str(v3) + " again!"
print("v3:", v3)
print("msg:", msg)

#列表
print("---list")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1].title())
#add
bicycles.append('hello')
bicycles.append('hello')
bicycles.insert(1, 'world')
#delete by index
del bicycles[0]
bicycles.pop(2)
#delete by value
rtn = bicycles.remove('hello')
print ('rtn:', rtn)
for bic in bicycles:
    print (bic)

