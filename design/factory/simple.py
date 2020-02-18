class phone:
    def __init__(self, name):
        self.name = name

    def show():
        pass

class XimoMiPhone(phone):
    def __init__(self, name):
        phone.__init__(self, name)

    def show(self):
        print("xiaomi phone:", self.name)

class HuaWeiPhone(phone):
    def __init__(self, name):
        phone.__init__(self, name)

    def show(self):
        print("huawei phone:", self.name)

class SimpleFactory:
    # def __init(self):
    #     pass

    def getphone(self, type_phone):
        if type_phone == 'xiaomi':
            return XimoMiPhone('xiaomi')
        elif type_phone == 'huawei':
            return HuaWeiPhone('huawei')
    
if __name__ == '__main__':
    factory = SimpleFactory()
    phone1 = factory.getphone('xiaomi')
    phone1.show()
    phone2 = factory.getphone('huawei')
    phone2.show()
