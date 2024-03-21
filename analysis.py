# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2019-11-14 下午2:44
import argparse
from rdao import Dao
from collections import Counter


class Forecast():
    def __init__(self):
        self.dao = Dao()

        parser = argparse.ArgumentParser(description='deliver COUNT')
        parser.add_argument('-c', '--cat', metavar='cattt', required=True, dest='input_count', action='append', help='set count for statistics')
        args = parser.parse_args()
        self.input_count = int(args.input_count[0])

        self.get()

    def get(self):
        number = self.dao.read()
        print(number)
        self.count(number)

    # red-blue: 01-33, 01-16
    # happy： 01-35, 01-12
    def count(self, number):
        first_number = number[::7]
        average = int(len(first_number) * 7 / 33)
        second_number = number[1::7]
        third_number = number[2::7]
        fourth_number = number[3::7]
        fifth_number = number[4::7]
        sixth_number = number[5::7]
        seventh_number = number[6::7]
        first_count = Counter(first_number).most_common(1).pop()
        second_count = Counter(second_number).most_common(1).pop()
        third_count = Counter(third_number).most_common(1).pop()
        fourth_count = Counter(fourth_number).most_common(1).pop()
        fifth_count = Counter(fifth_number).most_common(1).pop()
        sixth_count = Counter(sixth_number).most_common(1).pop()
        seventh_count = Counter(seventh_number).most_common(1).pop()
        result = [[first_count, second_count, third_count, fourth_count, fifth_count, sixth_count, seventh_count],
                  average]
        
        # [[('03', 2), ('07', 3), ('21', 2), ('27', 1), ('28', 1), ('32', 1), ('13', 2)], 1]
        print(result)
        self.divine(result)

    def divine(self, data):
        most_number = data[0]
        average = data[1]
        numbers = ''
        all_chance = 0
        for i in range(len(most_number)):
            number, count = most_number[i]
            probability = count / average * 100
            numbers += number + ' '
            all_chance += probability
        chance = round(all_chance / 7, 2)
        print("count = %d, 预测号码：%s"%(self.input_count, numbers.strip()))
        #print("中奖概率：%s" % chance + '%')
