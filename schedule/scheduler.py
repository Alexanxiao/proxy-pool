from .validator import Validator
from .adder import Adder
from core.db import DBManager
import time
from multiprocessing import Process

class Scheduler:

    def __init__(self):
        self._connection = DBManager()
        self._adder = Adder()
        self._validator = Validator()
        self._threshold = 200

    def schedule(self):
        print('proxy pool starts scheduling')
        while True:
            if self._connection.size<self._threshold:
                print('collecting free proxies')
                raw_proxies_ls = self._adder.add()
                for raw_proxies in raw_proxies_ls:
                    self._validator.recieve(raw_proxies)
                    self._validator.test()
                    self._connection.push(self._validator.useful_proxies)
            else:
                print('{} proxies left'.format(self._connection.size))
                self.circle_test()
                time.sleep(60)

    def circle_test(self):
        print('validating old proxies')
        proxies = self._connection.get(num=self._connection.size//3)
        for item in [proxies[i:i + 100] for i in range(0, len(proxies), 100)]:
            self._validator.recieve(item)
            self._validator.test()
            useful_proxies = self._validator.useful_proxies
            self._connection.push(useful_proxies)
