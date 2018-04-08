#!/usr/env/python3
# -*- coding:utf-8 -*-
# @Author : csl
# @Time   : 2017/12/02 12:21

print(ord('a'))
print(chr(97))
print(chr(0x61))
t = [0x8]
print(chr(t[0]))
print(ord(chr(t[0])))
print(chr(0x8))

test_array = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]
test_new_ivArray = ''
test_new_ivArray1 = ''
for i in test_array:
    test_new_ivArray += str(ord(chr(i)))
    test_new_ivArray1 += chr(i)
print(chr(test_array[7]))
print(test_new_ivArray)
print(test_new_ivArray1)
print(chr(0x61))