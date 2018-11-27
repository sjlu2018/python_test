# coding=utf-8
import sys
import os
import re
import struct

file = open(sys.argv[1])
fileout = open(sys.argv[1]+'2bin','w')

while 1:
    line = file.readline()
#    print(file)

    if not line:
        break
    pass # do something

#    arr=line.split(' ')
    arr=re.split(r'[\s]',line)
    src_bytes=struct.pack('i',int(arr[0]))
    fileout.write(src_bytes)
    
    dst_bytes=struct.pack('i',int(arr[1]))
    fileout.write(dst_bytes)
    
    #readline 读取文件的时候，默认加上“\n"
    weight_bytes=struct.pack('i',int(arr[2].replace('\n','')))
    fileout.write(weight_bytes)

file.close()
fileout.close()

