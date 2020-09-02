


def test_func1(p1, *param):
    print (p1)
    print (param)
    print (*param)

def test_func2(p1, p2, **pp):
    # print (p1)
    # print (p2)
    # print (pp)
    print (*pp)
    keyvals = ['%s=%s' % item for item in pp.items()]
    print (keyvals)
    for item in pp.items():
        print(item[0])

def test_func3(*args, **kwargs):
    print (args)
    print (kwargs)
    for item in kwargs.items():
        print(item[0], item[1])

a=1021
b="hello"
c=99
d='world'
e=["a", 'b', 'c']
# test_func1(a, b, c, d, e)

# [print ('%s%s' % i) for i in {size=99, a=199}]

# test_func2(a, b, size=100, large=99)
# test_func3(a, b, c, d, e, size=100, large=99, niubi=e)

f = a if a < c else c
print (f)

def add(x:int, y:int):
    print (x+y)
    return 1, 2, 3
what, x, z = add(100, 99)
print (what)

add = lambda x, y : x + y
what = add(52, 100)
print (what)

names = ['David Beazley', 'Brian Jones',
        'Raymond Aettinger', 'Ned Batchelder']
def sort_func(name):
    return name.split()[-1].lower()
# arr = sorted(names, key=lambda name: name.split()[-1].lower())
arr = sorted(names, key=sort_func)
print (arr)