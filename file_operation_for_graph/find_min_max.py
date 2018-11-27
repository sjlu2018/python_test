# coding=utf-8
import sys
import os
import re

file = open(sys.argv[1])
max_num = 0
min_num = 0xFFFFFFF
edge = 0
while 1:
    line = file.readline()

    if not line:
        break
    pass # do something
   
    #arr=line.split(' ')
    arr=re.split(r'[\s]',line)
    if arr[0].isdigit() and (arr[1].replace('\n','')).isdigit :
    	if max_num < int(arr[0]):
            max_num = int(arr[0])
        if max_num < int(arr[1].replace('\n','')):
            max_num = int(arr[1].replace('\n',''))

        if min_num > int(arr[0]):
            min_num = int(arr[0])
        if min_num > int(arr[1].replace('\n','')):
            min_num = int(arr[1].replace('\n',''))
        edge = edge+1
    else :
        print('not num,   line = '+str(edge))
        print(arr[0])
file.close()
print('max_num = '+str(max_num))
print('min_num = '+str(min_num))
print('edge = '+str(edge))

