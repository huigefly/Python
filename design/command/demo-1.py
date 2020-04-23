


# memory test
# cpu test
# netcard test
# ...

class test_factory:
    def mem_test(ui_update_cb):
        print ('mem testing')
        ui_update_cb(result)

    def cpu_test(ui_update_cb):
        print ('cpu testing')
        ui_update_cb(result)

    def netcard_test(ui_update_cb):
        print ('netcard testing')
        ui_update_cb(result)

if __name__ == "__main__":
    
    test_opt = get_from_ui()
    while (test_opt != 'exit'):
        test_factory = test_factory(ui_update_cb)
        if test_opt == "memory_test":
            test_factory.memory_test(ui_update_cb)
        else test_opt == "cpu_test":
            test_factory.cpu_test(ui_update_cb)
        else test_opt == "netcard_test":
            test_factory.netcard_test(ui_update_cb)
            
        test_opt = get_from_ui()