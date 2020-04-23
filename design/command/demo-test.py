'''
test_item.ini

[memory_test]
name="memory test"
obj_name=memory_test
other=....

[cpu_test]
name="cpu test"
obj_name=cpu_test
other=....

[netcard_test]         ----------< 新增， 修改点
name="netcard test"
obj_name=netcard_test
other=....

'''

class load_ini:
    def load(self, file_path):
        with open(file_path):
            #解析每一项测试项，保存属性
            item = parse_each_item()
            self.list_item_ini.add(item)
        return self.list_item_ini
    
    def get(item_name):
        # find ...
        return self.list_item_ini(item_name)

class item_test_base():
    def start_test():
        pass

class memory_test(item_test_base):
    def start_test():
        print('i am test memory')
        return result

class cpu_test(item_test_base):
    def start_test():
        print('i am test cpu')
        return result

class netcard_test(item_test_base):     #----------< 新增. 修改点
    def start_test():
        print('i am test netcard')
        return result


class test_item_manager:
    def add(item_ini):
        self.list_item_ini.add(item_ini)

    def remove(item)
        self.list_item_ini.remove(item)
    
    def notify():
        self._load()
        for item in self.list_item:
            item.start_test()
    
    def _load():
        for item_ini in self.list_item_ini:
            # 找到相应的测试对象， 如 memory_test
            test_obj = globals()[item_ini.get_obj_name()]
            self.list_item.add(test_obj)


if __name__ == '__main__':      #---------- < 稳定点

    # 加载测试项的配置文件
    list_test_items = load_ini.load(file_path)

    # ui界面上，可以利用name来显示测试项
    ui_update_test_items(list_test_items):

    # ui上选择相应的测试项
    item_name = ui_select_item()
    while (item_name != 'exit'):
        # 根据选择，找到相应的测试项的配置
        item_ini = load_ini.get(item_name)
        # 放入 item_manager
        test_item_manager.add(item_ini)

    test_item_manager.notify()