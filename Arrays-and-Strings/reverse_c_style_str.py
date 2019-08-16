#!/bin/env/py
# -*- coding: utf-8 -*-

def reverse_c_str(s):
    res = s[-2::-1]
    return res + "\0"
