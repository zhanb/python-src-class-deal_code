#!/user/bin/env python
#coding=utf-8
import sys
from sys import path
path.append('../class')
import deal_code as ConverCode

if __name__ == "__main__":
    length = len(sys.argv)
    if length != 3:
        print("python %s 1/2(1.u2g 2.g2u) file/dir"%sys.argv[:1][0])
        exit()
    flag = sys.argv[1:][0]
    path = sys.argv[1:][1]
    print(flag,path)
    myConver = ConverCode.conver(path,flag)
    myConver.deal_conver()
