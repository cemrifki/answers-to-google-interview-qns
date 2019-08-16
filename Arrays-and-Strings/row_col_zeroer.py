#!/env/bin/py
# -*- coding: utf-8 -*-



def col_row_zeroer(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                row = 0
                while row < len(m):
                    m[row][j] = -1
                    row += 1
                col = 0
                while col < len(m[i]):
                    m[i][col] = -1
                    col += 1
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == -1:
                m[i][j] = 0
    return m
