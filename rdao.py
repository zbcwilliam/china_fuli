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
        hash_table = {'r01': 0, 'r02': 0, 'r03': 0, 'r04': 0, 'r05': 0,
                      'r06': 0, 'r07': 0, 'r08': 0, 'r09': 0, 'r10': 0,
                      'r11': 0, 'r12': 0, 'r13': 0, 'r14': 0, 'r15': 0,
                      'r16': 0, 'r17': 0, 'r18': 0, 'r19': 0, 'r20': 0,
                      'r21': 0, 'r22': 0, 'r23': 0, 'r24': 0, 'r25': 0,
                      'r26': 0, 'r27': 0, 'r28': 0, 'r29': 0, 'r30': 0,
                      'r31': 0, 'r32': 0, 'r33': 0,
                      'b01': 0, 'b02': 0, 'b03': 0, 'b04': 0, 'b05': 0,
                      'b06': 0, 'b07': 0, 'b08': 0, 'b09': 0, 'b10': 0,
                      'b11': 0, 'b12': 0, 'b13': 0, 'b14': 0, 'b15': 0, 'b16': 0}
        date_keys = self.conn.keys()
        date_keys.sort()
        for date_key in date_keys:
            # if date_key.startswith('2402'):
            #     print(date_key)
        # if date_key.startswith('2402'):    
            value = self.conn.get(date_key)
            number_list = value.split("#")[0].split('_')
            for index, number in enumerate(number_list):
                if index == 6:
                    hash_table['b'+number] = hash_table['b'+number] + 1
                else:
                    hash_table['r'+number] = hash_table['r'+number] + 1
                    
            onehit_item = ''        
            list_count_ball = []
            for key, value in hash_table.items():
                # print(f"Key: {key}, Value: {value}")
                
                onehit_item = onehit_item + (key + '-' + str(value) + '; ')
                list_count_ball.append(str(value) + '-' + key)
                
            print(f"{date_key}#{number_list}#{onehit_item}")
            

            list_count_ball.sort()
            onehit_item2 = ''
            for count_ball in list_count_ball:
                if onehit_item2 == '':
                    onehit_item2 = count_ball + "; "
                else:
                    onehit_item2 = onehit_item2 + count_ball + "; "
                
            print(f"{date_key}#{number_list}#{onehit_item2}")      
            
            print("\n")
                
            all_number += number_list
         
        # totolhit_item = ''    
        # for key, value in hash_table.items():
        #     totolhit_item = totolhit_item + (key + '-' + str(value) + '; ')
        # print(f"{totolhit_item}")       

        #print(all_number) 
        return all_number
