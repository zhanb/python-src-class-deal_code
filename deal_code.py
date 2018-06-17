#!/user/bin/env python
#coding=utf-8
import os,sys
import chardet
class conver:
    def __init__(self,path,deal_flag):
        self.filelist = []
        self.deal_flag = deal_flag
        if os.path.isfile(path):
            self.filelist.append(path)
        elif os.path.isdir(path):
            self.path = path
            self.getFile()
    def getFile(self):
        for root,dirs,files in os.walk(self.path):
            for file in files:
                self.filelist.append(os.path.join(root,file))
    def deal_conver(self):
        if self.deal_flag == '1':
            for file in self.filelist:
                self.u2g(file)
        elif self.deal_flag == '2':
            for file in self.filelist:
                self.g2u(file)
        else:
            print('flag err'+self.deal_flag)
    def u2g(self,file):
        content = open(file).read()
        result = chardet.detect(content)#通过chardet.detect获取当前文件的编码格式串，返回类型为字典类型
        coding = result.get('encoding')#获取encoding的值[编码格式]
        print(file,coding)
        new_content = content.decode(coding).encode('GBK')
        open(file, 'w').write(new_content)
    def g2u(self,file):
        content = open(file).read()
        result = chardet.detect(content)#通过chardet.detect获取当前文件的编码格式串，返回类型为字典类型
        coding = result.get('encoding')#获取encoding的值[编码格式]
        print(file,coding)
	new_content = content.decode(coding).encode('UTF8')
        open(file, 'w').write(new_content)
