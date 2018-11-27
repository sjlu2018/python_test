# coding=utf-8
import sys
import os
import re
import struct

file = open(sys.argv[1],'rb')
fileout = open(sys.argv[1]+'.2str0','w')
#src1 = int(file.read(4))
#src2 = int(file.read(4))
#weight = int(file.read(4))
(src1,) = struct.unpack('i',file.read(4))
(src2,) = struct.unpack('i',file.read(4))
(weight,) = struct.unpack('i',file.read(4))

while src1 >0 or src2>0 or weight>0 :
    fileout.write(str(src1))
    fileout.write(' ')
    fileout.write(str(src2))
#    fileout.write(' ')
#    fileout.write(str(weight))
    fileout.write('\n')
    (src1,) = struct.unpack('i',file.read(4))
    (src2,) = struct.unpack('i',file.read(4))
    (weight,) = struct.unpack('i',file.read(4))

file.close()
fileout.close()

