#!/bin/env/py
# -*- coding: utf-8 -*-

from collections import Counter

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    for i in range(len(s1_sorted)):
        if s1_sorted[i] != s2_sorted[i]:
            return False

    return True

def anagram2(s1, s2):
    if len(s1) != len(s2):
        return False

    s1 = Counter(s1)
    s2 = Counter(s2)

    for c in s1:
        if c not in s2:
            return False
        if s1[c] != s2[c]:
            return False

    for c in s2:
        if c not in s1:
            return False
        if s1[c] != s2[c]:
            return False

    return True
    
