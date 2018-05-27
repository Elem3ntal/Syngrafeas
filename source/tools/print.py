#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_dict(arg, prefig=""):
    for key in arg:
        output_key = "['{KEY}']" if type(key) is str else "[{KEY}]"
        if type(arg[key]) is not dict:
            output_format = "{PREFIG}"+output_key+": {TEXT}"
            print(output_format.format(PREFIG=prefig, KEY=key, TEXT=arg[key]))
        else:
            output_prefig = output_format
            print_dict(arg=arg[key], prefig=output_key.format(KEY=key))

def print_modify(*args):
    for arg in args:
        if type(arg) in [list, set]:
            print(arg)
            for element in arg:
                print(element)
        elif type(arg) in [dict]:
            print_dict(arg)


print_modify({0,1,2,3},{"a":1,
                        "b":2,
                        0:3,"other_dict":{"inter":"vlaue"}},[1,2,3,4],"asd")
print(type({}) is dict)