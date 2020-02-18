class phone:
    def __init__(self, name):
        self.name = name

    def show():
        pass

class XiaomiPhone(phone):
    def __init__(self, name):
        phone.__init__(self, name)

    def show(self):
        print("xiaomi phone:", self.name)

class HuaWeiPhone(phone):
    def __init__(self, name):
        phone.__init__(self, name)

    def show(self):
        print("huawei phone:", self.name)

class route:
    def __init__(self, name):
        self.name = name

    def wifi(self):
        pass

class XiaomiRoute(route):
    def __init__(self, name):
        route.__init__(self, name)
    
    def wifi(self):
        print('%s wifi' % self.name)

class HuaweiRoute(route):
    def __init__(self, name):
        route.__init__(self, name)
    
    def wifi(self):
        print('%s wifi' % self.name)

class Factory:
    # def __init(self):
    #     pass

    def createPhone(self):
        pass

    def createRoute(self):
        pass

class XiaomiFactory(Factory):
    def createPhone(self):
        return XiaomiPhone('xiaomi')
    
    def createRoute(self):
        return XiaomiRoute('xiaomi')


class HuaweiFactory(Factory):
    def createPhone(self):
        return HuaweiPhone('huawei')
    
    def createRoute(self):
        return HuaweiRoute('huawei')
    
if __name__ == '__main__':
    factory = XiaomiFactory()
    phone = factory.createPhone()
    phone.show()
    factory2 = HuaweiFactory()
    route = factory2.createRoute()
    route.wifi()
