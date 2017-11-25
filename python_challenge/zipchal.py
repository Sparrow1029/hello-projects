#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zipfile import ZipFile
import re

f = ZipFile('channel.zip')
num = '90052'  # collect the comments
comments = []

while True:
    content = f.read(num + ".txt").decode("utf-8")
    comments.append(f.getinfo(num + '.txt').comment.decode('utf-8'))
    print(content)
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))
