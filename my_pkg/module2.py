#!/usr/bin/python3

import re

def clean(tmp_list):
    numbers = re.findall("\d", tmp_list)
    
    return numbers


def unionfunction(list1, list2):
    union_tmp = list(set(list1).union(list2))
    print('union:', end='')
    print(union_tmp)


def interfunction(list1, list2):
    inter_tmp = list(set(list1).intersection(list2))
    print('intersection:', end='')
    print(inter_tmp)
    
