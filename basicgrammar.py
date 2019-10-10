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
rtn = bicycles.remove('helloa')
print ('rtn:', rtn)
for bic in bicycles:
    print (bic)