# coding=utf-8
import sys
import os
import re

print('transform:',sys.argv[1])

file = open(sys.argv[1])
fileout = open(sys.argv[1]+'tran0','w')
 
while 1:
    line = file.readline()
#    print(file)

    if not line:
        break
    pass # do something
   
#    arr=line.split(' ')
    arr=re.split(r'[\s]',line)
    fileout.write(str(int(arr[0])+1))
    fileout.write(' ')
    #readline 读取文件的时候，默认加上“\n"
    fileout.write(str(int(arr[1].replace('\n',''))+1))
    fileout.write('\n')

file.close()
fileout.close()

