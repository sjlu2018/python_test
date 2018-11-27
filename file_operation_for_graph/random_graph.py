# coding=utf-8
#python ./random_graph.py random.txt0 100 200
#         本程序名         输出文件名 顶点 边
import sys
import os
import random

src_max  = 0;
dest_max = 0;

fileout = open(sys.argv[1],'w')
for i in range(1,int(sys.argv[3])):
    src  = random.randint(1,int(sys.argv[2]))
    dest = random.randint(1,int(sys.argv[2]))
    
    fileout.write(str(src))
    fileout.write(' ')
    fileout.write(str(dest))
    fileout.write('\n')

    if src > src_max :
        src_max = src;
    if dest > dest_max :
        dest_max = dest;

fileout.write(sys.argv[2])
fileout.write(' ')
fileout.write(str(random.randint(1,int(sys.argv[2])-1)))
fileout.write('\n')

fileout.close()

