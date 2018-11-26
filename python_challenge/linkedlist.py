#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, re


base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

def find_nothing(url, num):
    url = url + num
    txt = requests.get(url + num).content.decode('utf-8')
    print(txt)
    mo = re.search('and the next nothing is (\d+)', txt)
    if mo == None:
        print(txt)
        return
    next_url = mo.group(1)
    # print(next_url)
    return(next_url)

cnt = 400
x = find_nothing(base_url, '12345')
while cnt > 0:
    y = find_nothing(base_url, x)
    x = find_nothing(base_url, y)
    print(cnt)
    cnt -= 1

# print(a[0]['href'])

