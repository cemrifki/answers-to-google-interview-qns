#!/bin/env/py
# -*- coding: utf-8 -*-

def isSubtring(s1, s2):
    if len(s1) > len(s2):
        long_str = s1
        short_str = s2
    else:
        long_str = s2
        short_str = s1
    return short_str in long_str
def isRotated(s1, s2):
    if len(s1) != len(s2) or s1 == None or s2 == None:
        return False
    s2 *= 2
    return s1 in s2
