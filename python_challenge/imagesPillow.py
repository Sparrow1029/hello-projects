#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

img = Image.open("oxygen.png")

print(img.width, img.height)
# img.show()

row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
# for i in row[::7]:
#     print(i)
ords = [r for r,g,b,a in row[::7] if r==g==b]
# print(ords)

answer = ''.join(map(chr, ords))

import re

nums = re.findall("\d+", answer)
print(''.join(map(chr, map(int,nums))))
