#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:24:33 2020

@author: jonathanzeas

This program creates a Hill Cypher and encyphers text


"""
import numpy as np
import re

letters_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
finished_arr = []

#key values for encryption
key1 = 9
key2 = 4
key3 = 5
key4 = 7

#text to encrypt
text = "crypto class is at three oclock but it is virtual"

#remove non alphanumeric characters from the string
text = re.sub('[\W_]', '', text)

key_arr = np.array([[key1, key2],[key3, key4]])

#add a q if needed
if (len(text)%2 == 1):
    text = text+"q"



to_be_encrpyt_nums = []    

##convert to numbers, add to array
for i in text:
    num = letters_arr.index(i)
    to_be_encrpyt_nums.append(num)
    
#convert to matrix, dot with key, append result
while len(to_be_encrpyt_nums) > 0:
    temp_arr = np.array([[to_be_encrpyt_nums.pop(0)], [to_be_encrpyt_nums.pop(0)]])
    result_arr = np.dot(key_arr, temp_arr)
    finished_arr.append(letters_arr[result_arr[0][0]%26])
    finished_arr.append(letters_arr[result_arr[1][0]%26])

#convert result to text
result = ""    
for i in finished_arr:
    result+= i

print(result)

