# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2019-11-14 下午2:30
import redis
import operator

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
            for key, value in hash_table.items():
                if key == 'r33':
                    onehit_item = onehit_item + (key + '-' + str(value) + ' |---| ')
                else:
                    onehit_item = onehit_item + (key + '-' + str(value) + '; ')
                
            print(f"{date_key}#{number_list}#{onehit_item}")
            
            # sort red balls , sort blue balls        
            red_blue_keys = list(hash_table.keys())
            red_keys = red_blue_keys[:33]
            blue_keys = red_blue_keys[33:]

            dict_red  = {k: hash_table[k] for k in red_keys}
            dict_blue = {k: hash_table[k] for k in blue_keys}
            
            sorted_dict_red  = dict(sorted(dict_red.items(), key=operator.itemgetter(1)))
            sorted_dict_blue = dict(sorted(dict_blue.items(), key=operator.itemgetter(1)))
            
            onehit_item3_red = ''
            count_key = 0
            
            number_list_hit_red  = number_list[:6]
            number_list_hit_blue = number_list[6:]
            
            for key, value in sorted_dict_red.items():
                count_key = count_key + 1
                
                # key such as: r01-533
                red_key = key.split('-')[0][1:]
                new_red_key = key
                
                flag_hit = False
                for one_hit_ball in number_list_hit_red:
                    if red_key == one_hit_ball:
                        flag_hit = True
                        new_red_key = 'R' + red_key
                
                if count_key == 33:
                    onehit_item3_red = onehit_item3_red + (new_red_key + '-' + str(value) + ' |---| ')
                else:
                    onehit_item3_red = onehit_item3_red + (new_red_key + '-' + str(value) + '; ')


            # handle blue
            onehit_item3_blue = ''            
            for key, value in sorted_dict_blue.items():
                
                # key such as: b01-533
                blue_key = key.split('-')[0][1:]
                new_blue_key = key
                
                flag_hit = False
                for one_hit_ball in number_list_hit_blue:
                    if blue_key == one_hit_ball:
                        flag_hit = True
                        new_blue_key = 'B' + blue_key
                
                onehit_item3_blue = onehit_item3_blue + (new_blue_key + '-' + str(value) + '; ')
                
            print(f"{date_key}#{number_list}#{onehit_item3_red}{onehit_item3_blue}")      
            
            print("\n")

            # list_count_ball.sort()
            # onehit_item2 = ''
            # for count_ball in list_count_ball:
            #     if onehit_item2 == '':
            #         onehit_item2 = count_ball + "; "
            #     else:
            #         onehit_item2 = onehit_item2 + count_ball + "; "
                
            # print(f"{date_key}#{number_list}#{onehit_item2}")      
            
            # print("\n")
                
            all_number += number_list
         
        # totolhit_item = ''    
        # for key, value in hash_table.items():
        #     totolhit_item = totolhit_item + (key + '-' + str(value) + '; ')
        # print(f"{totolhit_item}")       

        #print(all_number) 
        return all_number
