#!/usr/bin/python2.7

from collections import defaultdict

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)
            
# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)

# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]

class Task:
    def __init__(self, name):
        self.__name = name

    def send(self, msg):
        print("task msg:", self.__name, msg)

if "__main__" == __name__:
    task_a = Task('a')
    task_b = Task('b')

    # Example of getting an exchange
    exc = get_exchange('name')

    # Examples of subscribing tasks to it
    exc.attach(task_a)
    exc.attach(task_b)

    # Example of sending messages
    exc.send('msg1')
    exc.send('msg2')

    # Example of unsubscribing
    exc.detach(task_a)
    exc.detach(task_b)