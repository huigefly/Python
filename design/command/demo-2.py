


# memory test
# cpu test
# netcard test
# ...

class test_factory:
    def mem_test():
        print ('mem testing')
        return result

    def cpu_test():
        print ('cpu testing')
        return result

    def netcard_test():
        print ('netcard testing')
        return result

class cmd_base:
    def __init__(test_factory):
        self.test_factory = test_factory
    
    def exec():
        pass

class cmd_mem(cmd_base):
    def exec():
        self.test_factory.mem_test()

class cmd_cpu(cmd_base):
    def exec():
        self.test_factory.cpu_test()

class cmd_netcard(cmd_base):
    def exec():
        self.test_factory.netcard_test()


class record:
    def set(cmd):
        self.list_cmd.add(cmd)
    
    def remove(cmd):
        self.list_cmd.remove(cmd)
    
    def notify():
        result = ''
        for cmd in list_cmd:
            result += cmd.exec()
        return result

class cmd_factory:
    
    def get(type, test_factory):
        if type == 'mem':
            return cmd_mem(test_factory)
        elif type == 'cpu':
            return cmd_cpu()
        elif type == 'netcard':
            return cmd_netcard()

if __name__ == "__main__":

    map_test_obj = {'1': 'mem_test', 
                    '2': 'cpu_test',
                    '3': 'netcard_test' }
    test_opt = get_from_ui()
    record = record()
    test_factory = test_factory()
    while (test_opt != 'start'):
        record.set(cmd_factory.get(test_opt, test_factory)
        test_opt = get_from_ui()
    
    result = record.notify()
    ui_update(result)