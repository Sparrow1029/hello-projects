#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = '1'
b = ''

for _ in range(30):
    j, k = 0, 0
    while j < len(a):
        while k < len(a) and a[k] == a[j]:
            k += 1
        b += str(k-j) + a[j]
        j = k
    print(b)
    a = b
    b = ''
print(len(a))
