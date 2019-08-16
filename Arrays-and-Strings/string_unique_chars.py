#!/bin/env/py
# -*- coding: utf-8 -*-

def has_all_unique(s):
    if len(s) == 1 or not s:
        return True
    s = s.lower()
    res = ''.join(sorted(s))
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            return False
    return True
