import redis
from .config import *

class DBManager:

    def __init__(self):
        self._db_name = db_name
        self._connection = redis.Redis(host=HOST, port=PORT)

    def push(self, proxies):
        self._connection.sadd(self._db_name, *proxies)

    def get(self, num=1):
        '''
        取出代理，但不删除
        :param num: 取出个数
        :return: 代理
        '''
        if num > self.size:
            num = self.size
        temp = self._connection.srandmember(self._db_name, num)
        return [item.decode('utf-8') for item in temp]

    def pop(self):
        '''
        取出代理并删除
        :param num: 取出个数
        :return: 代理
        '''
        return self._connection.spop(self._db_name).decode('utf-8')

    def flush(self):
        self._connection.flushall()

    @property
    def size(self):
        return self._connection.scard(self._db_name)
