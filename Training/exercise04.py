
# !/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys

f = open(str(sys.argv[1]), 'r+')
filedata = f.read()

# Lets create a pattern and extract some information with it
regex_entity = re.compile(r"<entity name=\"(.*)\">")
regex_marriedTo = re.compile(r"(husband|marriage|daughter).*<entity name=\"(.*)\">")

result_entity = regex_entity.search(filedata)
result_marriedTo = regex_marriedTo.search(filedata)

if result_entity:
    # print(result_entity.group(0))
    print(result_entity.group(1))
    # print(result_entity.group(2))
    # print(result_entity.group(0))
    print("\n")
else:
    print("NO result_marriedTo")

if result_marriedTo:
    # print(result_marriedTo.group(0))
    print(result_marriedTo.group(1))
    print(result_marriedTo.group(2))
    # print(result_marriedTo.group(0))
    print("\n")
else:
    print("NO result_marriedTo")


# if result_entity:
#     if result_marriedTo:
#         print(result_marriedTo.group(2))
#         tuple_entity_marriedTo = (result_entity.group(0), "marriedTo", result_marriedTo.group(2))
#         print(tuple_entity_marriedTo)
#     else:
#         print("NO is-a type")





















