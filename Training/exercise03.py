
# !/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
import nltk

f = open(str(sys.argv[1]), 'r+')
filedata = f.read()

# Lets create a pattern and extract some information with it
regex_entity = re.compile(r"http://en.wikipedia.org/wiki/([a-zA-Z_]+)")
regex_is_a = re.compile(r"(is a|is an|was an|was a) ([a-zA-Z-_ ]+)")

result_entity = regex_entity.search(filedata)
result_is_a = regex_is_a.search(filedata)

if result_entity:
    if result_is_a:
        print(result_is_a.group(2))
        tuple_entity_is_a = (result_entity.group(0), "is a", result_is_a.group(2))
        print(tuple_entity_is_a)
    else:
        print("NO is-a type")






















