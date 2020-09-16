#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:21:35 2020

@author: jonathanzeas
"""

import numpy as np
import re

letters_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
finished_arr = []

inv_key1 = 5
inv_key2 = 12
inv_key3 = 15
inv_key4 = 25

enc_text = "izqrtlkjuwmqgmnubyawegzxgclpvvvvmdkdrbsz"

inv_key_arr = np.array([[inv_key1, inv_key2],[inv_key3, inv_key4]])

to_be_decrpyt_nums = []  

for i in enc_text:
    num = letters_arr.index(i)
    to_be_decrpyt_nums.append(num)
    
while len(to_be_decrpyt_nums) > 0:
    temp_arr = np.array([[to_be_decrpyt_nums.pop(0)], [to_be_decrpyt_nums.pop(0)]])
    result_arr = np.dot(inv_key_arr, temp_arr)
    finished_arr.append(letters_arr[int(result_arr[0][0])%26])
    finished_arr.append(letters_arr[int(result_arr[1][0])%26])

#convert result to text
result = ""    
for i in finished_arr:
    result+= i

print(result)
