
# !/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys

f = open(str(sys.argv[1]), 'r+')
filedata = f.read()


def decide_month(x):
    return {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12',
    }.get(x, '00')    # 9 is default if x not found

# Lets create a pattern and extract some information with it
regex_entity = re.compile(r"http://en.wikipedia.org/wiki/([a-zA-Z_]+)")
regex_data = re.compile(r"born (\d+) ([a-zA-Z]+ \d+)*")
regex_data_2 = re.compile(r"\((\d+) ([a-zA-Z]+ \d+)*")

result_entity = regex_entity.search(filedata)
print(result_entity.group(0))

bd_date = ""
date = re.search(regex_data, filedata)
if date:
    print(date.group(0))
    bd_date = date
else:
    date_2 = re.search(regex_data_2, filedata)
    if date_2:
        print(date_2.group(0))
        bd_date = date_2


birthday = ""
date_composant_list = []

if result_entity:
    if bd_date:
        date_composant_list = bd_date.group(0).split(" ")
        if date_composant_list[0] != 'born':
            date_composant_list[0] = date_composant_list[0].replace('(', '')
        else:
            date_composant_list.remove(date_composant_list[0])
        if len(date_composant_list) == 3:
            birthday = date_composant_list[2] + "-" + decide_month(date_composant_list[1]) + "-" + date_composant_list[0]
        else:
            birthday = date_composant_list[0]
        tuple_entity_date = (result_entity.group(0), "hasDate", birthday)
        print(tuple_entity_date)
    else:
        print("No hasDate")
























