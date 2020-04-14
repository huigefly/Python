# -*- coding: utf-8 -*-
import os
import json
from collections import namedtuple as _namedtuple


a=1
def aa(s):
	return 1 if s == 1 else 0
print aa(0)


'''
v=1
a=2
b=3
if v == 2 or (a == 2 and b == 3):
    print("ok")
os._exit(0)

state = {'00000000-0000-0000-0000-000000000001': {'621dc693-73f4-4338-9e50-1dc118d21c7e': {'state': 'HEALTH', 'timestamp': 1582874215}}}
print(state["00000000-0000-0000-0000-000000000001"])
if "00000000-0000-0000-0000-000000000001" in state:
    print("have in ")
else:
    print("no in")

os._exit(0)







_DISK_STATES = ['HEALTH', 'TROUBLE', 'UNKNOWN']
_DISK_STATE_ENUM = _namedtuple('_DiskStateEnum', _DISK_STATES)
DISK_STATE = _DISK_STATE_ENUM(*_DISK_STATES)
print (DISK_STATE)
print(DISK_STATE.HEALTH)
print


s = {"nodeid": {"disk_sn1": {"state": "state1", "timestamp": 123}, "disk_sn2": {"state": "state2", "timestamp": 456},}}
for i in s["nodeid"]:
    print(i)

print

ctt = "{ \
    \"host_id\": \"3984d05e-4da7-4731-8ef6-65afc1b24181\", \
    \"timestamp\": 1234567890123, \
    \"disk_list\": [\
    {\
         \"disk_sn\":\"BTWL3303032C160MGN\",\
         \"name\": \"sda\",\
         \"state\": \"HEALTH\",\
         \"wear_leveling_count\":{\
             \"value\":99,\
             \"worst\":99,\
             \"threshold\":0\
          },\
          \"media_wearout_indicator\": None\
    }\
]\
}"
print(json.dumps(ctt))
print
print

_states = {
    "1234d05e-4da7-4731-8ef6-65afc1b24181":
    {
         "3984d05e-4da7-4731-8ef6-65afc1b24181":
         {
             "state": "HEALTH",
             "timestamp": 1234567890123,
         },
    }
}

print(len(_states))

b = "bb"
a = "aa"
l = {}
if a in l and a in l["aa"]:
    print "gdo"
else:
    print "bad"

#a = {"nihaoshijie":{"state":"good", "time":11024}}
#sta={}
#sta.update(a)
#print(sta)
#a = {"nihaoshijie":{"state":"bad", "time":11024}}
#sta.update(a)
##print(sta)
#a = {"helloaaaaa":{"state":"gsood", "time":11024}}
#sta.update(a)
#print(sta)

##print
#print
info = {"helloworld":{"nihaoshijie":{"state":"good", "time":11024}}}
st={}
st.update(info)
print(st)
info = {"helloworld":{"what":{"state":"bad", "time":1221024}}}
st["helloworld"].update(info["helloworld"])
print(st)
info = {"helloworld":{"what":{"state":"sssbad", "time":1221024}}}
st["helloworld"].update(info["helloworld"])
print(st)

for i in st["helloworld"]:
    st["helloworld"][i]["state"] = "shenemdongxia"
print(st)

print 
print
#info = {"shenme":{"keyi":{"state":"bad", "time":1221024}}}
#st.update(info)
#print(st)

class a0221:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item, section=None):
        print('getattr:', item)
        print('section:', section)
        return item

a = a0221('hello')
print(a.name)
print(a.what)
print(a.hellworold('good'))

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

class a:
    al = []
    def __init__(self):
        self._nl = "helloworld"
        self.__sl = "nihaoshijie"

s = a()
print(s._nl)

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


# 变量
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
'''
