#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : chensl
# @Time    : 2017/2/28 15:18
'''接口加解密过程'''

from pyDes import des,CBC,PAD_PKCS5
import base64
class interfaceDes:

    def __init__(self,key,ivArray):
        # key 密钥
        # ivArray 偏移量
        self.key = key
        self.ivArray = ivArray

    # 加密方法
    def get_encrypt_data(self,data):
        self.new_ivArray = ''
        for i in self.ivArray:
            self.new_ivArray += chr(i)  #返回对应i值的对应输出码,chr()用一个范围在range(256)内的(就是0～255)整数作参数，返回一个对应的字符。

        self.temp = des(self.key, CBC, self.new_ivArray, pad=None, padmode=PAD_PKCS5)  #实例化des对象
        encrypt_data = self.temp.encrypt(data, pad=None, padmode=PAD_PKCS5)  #调用encrypt方法对参数进行加密
        # print(encrypt_data)
        return base64.b64encode(encrypt_data)  # 返回64位编码加密结果

    # 解密方法
    def get_decrypt_data(self,data):

        # data = data.replace('','+') #重写字符中的 '' 为 +
        data = base64.b64decode(data)  #编码转换
        return self.temp.decrypt(data=data)

if __name__ == '__main__':
    interfaceDestest = interfaceDes('4bbd85de',[0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8])
    name=dict(b=100,c='jack',a='lili',d='csl')  #创建参数字典
   # print(sorted(name.items()))
    import json
    # JSONEncoder().encode(d)将Python dict类型转换成标准Json字符串
    # JSONDecoder().decode(json_str)将json字符串转换成Python dict类型
    # k = json.JSONEncoder().encode(name)
    encrypt_test = interfaceDestest.get_encrypt_data(json.JSONEncoder().encode(name))
    print('加密编码后的字符为:%s' % encrypt_test)
    decrypt_test = interfaceDestest.get_decrypt_data(encrypt_test)
    print('解密编码后的字符为:%s' % decrypt_test)