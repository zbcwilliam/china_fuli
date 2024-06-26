# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2019-11-14 下午2:30
import redis

from settings import *


class Dao():
    def __init__(self):
        self.conn = redis.Redis(host=HOST, port=PORT, decode_responses=True)

    def flush_db(self):
        self.conn.flushdb()

    def write(self, name, value):
        self.conn.set(name, value)

    def read(self):
        all_number = []
        keys = self.conn.keys()
        for key in keys:
            value = self.conn.get(key)
            number_list = value.split("#")[0].split('_')
            all_number += number_list

        #print(all_number) 
        return all_number
