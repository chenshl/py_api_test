#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : csl
# @Time    : 2017/3/14 16:00
from common.interfaceDes import interfaceDes
from common.request2jww import request2jww as baserequest
import hashlib,requests,json

class request2jwwstrict(baserequest):
    global key2,desKey,ivArray  #定义全局变量
    key2 = '23be21a033d59833d3d87426a869e5ec'
    desKey = '4bbd85de'
    ivArray = [0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]  #定义16进制数组

    def send(self):
        self.sortapiParam = self.sortParam()  #继承自request2jww的sortParam()方法，将参数按照key值进行排序
        self.sortPriParam = self.getPriParam()  #返回字典形式数据
        r = requests.post(self.get_fullAPIUrl(self.apiName), self.sortPriParam)  #实例化post请求
        if r.status_code == 200:
            self.body = r.json()
            # if self.body['result'] == str(1):
            #     print(self.body)
            # else:
            #     print('请求返回失败')
            #     print(self.body)
        print(self.body)
        return self.body

    # 获取密文参数
    def getPriParam(self):
        interfaceDestest = interfaceDes(desKey,ivArray)  #实例化加密对象
        self.str = ''
        for i in self.sortapiParam:
            self.str += str(i[1])  #获取参数key值拼接成字符串
        m = hashlib.md5()  #生成一个md5 hash对象
        # 生成hash对象后，用update方法对字符串进行md5加密的更新处理
        m.update(key2.encode('utf-8')+self.str.encode('utf-8'))
        sign = m.hexdigest()  #16进制的加密结果字符串
        #调用interfaceDes类的加密方法进行参数加密，self.apiParam为继承自request2jww的__init__()方法
        names = interfaceDestest.get_encrypt_data(json.JSONEncoder().encode(self.apiParam))
        return dict(sign=sign,names=names)

if __name__ == '__main__':
    apiname = '/m/php/shop/forgetPayPasswordPhp'
    apiParam = {'userId':'000065bc-bcb2-11e5-b300-d89d672713e0',
                'Password':111111,
                'repeatPayPassword':543578,
                'smsCode':1234}

    request2jwwstrict(apiName=apiname, apiParam=apiParam).send()