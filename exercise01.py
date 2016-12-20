
# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import nltk
import re
#########################################################################
#  create a dictionary of {[entity_name, URI_de_entity_name]}
#########################################################################

with open('entity_list.txt') as f:
    content = f.readlines()

lines = []
for each_line in content:
    lines.append(each_line.strip('\n'))

dict_entity_name_URI = {}
#########################################################################
#  start to extract the NNP entities from the .txt files
#  create a list of entity names
#########################################################################
file = str(sys.argv[1])
newFile = file.split('/')[-1].split('.')[0] + "_2.txt"

f = open(file, 'r')
sample = f.readlines()
f.close()

patterns = """
    NP: {<DT|PP\$>?<JJ>*<NN>}
        {<NNP>+}
        {<NN>+}
"""
NPChunker = nltk.RegexpParser(patterns)  # create a chunk parser

f = open(file, 'r')
filedata = f.read()
f.close()

# a tree traversal function for extracting NP chunks in the parsed tree


def traverse(t):
    each_entity_name = []
    try:
        t.label
    except AttributeError:
        return
    else:
        if t.label() == 'NP':
            # print("t : ", t)  # (NP Vanessa/NNP Paradis/NNP)
            # child : ('Vanessa', 'NNP')
            # child : ('Paradis','NNP')
            nnp_child_name = ""
            for child in t:
                if child[1] == 'NNP':
                    nnp_child_name = nnp_child_name + child[0] + " "
                    nnp_child_name = nnp_child_name.replace('\n', '')
                    nnp_child_name = nnp_child_name.replace('\t', '')
                    nnp_child_name = nnp_child_name.strip('\n')
                    nnp_child_name = nnp_child_name.strip('_')
            if nnp_child_name != "":
                nnp_child_name = nnp_child_name.replace(' ', '_').strip('_').replace('_', ' ')
                each_entity_name.append(nnp_child_name)
                nnp_child_name_URI = 'http://en.wikipedia.org/wiki/' + nnp_child_name.replace(' ', '_').strip('_')
                for each_URI in lines:
                    if each_URI == nnp_child_name_URI:
                        nnp_child_name_lists = []
                        nnp_child_name_lists.append(nnp_child_name)
                        nnp_child_name_lists += nnp_child_name.split(" ")
                        for l in nnp_child_name_lists:
                            dict_entity_name_URI[l] = nnp_child_name_URI
        else:
            for child in t:
                traverse(child)

for line in sample:
    tokenized_words = nltk.word_tokenize(line)
    tagged_words = nltk.pos_tag(tokenized_words)
    result = NPChunker.parse(tagged_words)
    traverse(result)

keys = dict_entity_name_URI.keys()

# define desired replacements here
rep = {}
for key in keys:
    key_URI = "<entity name=\"" + dict_entity_name_URI[key] + "\">" + key + "</entity>"
    rep[key] = key_URI

# use these three lines to do the replacement
rep = dict((re.escape(k), rep[k]) for k in rep.keys())
pattern = re.compile("|".join(rep.keys()))
filedata = pattern.sub(lambda m: rep[re.escape(m.group(0))], filedata)


result_file = open(newFile, 'w')
result_file.write(filedata)












