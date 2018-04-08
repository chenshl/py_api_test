#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : csl
# @Time    : 2017/3/15 16:26
import requests
from random import Random
import hashlib
import copy
class request2jvv(object):

    def __init__(self,service,param):
        # service 接口名称
        # param 接口参数，字典形式
        self.url = 'http://192.168.1.8:6080/service' #服务器地址
        self.pubparam = {
            'buildVersion': '100',
            'device': 'Python',
            'deviceId': 'Python34',
            'partnerId': '20170315123001000001',
            'system': 'python',
            'systemVersion': '3.4',
        }
        self.pubparam['service'] = service #添加接口参数
        self.pubparam['orderNo'] = self.get_rand_string() #添加随机orderNo
        for k,v in param.items(): #添加接口请求参数
            self.pubparam[k] = v
        self.secsign = copy.deepcopy(self.pubparam) #深度拷贝公共参数部分
        self.secsign['publicKey'] = '51face7d5d52497016e7865c052ac051'  #sign生成添加公钥
        self.signlist = sorted(self.secsign.items())  #将参数按照key值进行排序
        self.str = ''
        for i in self.signlist:
            self.str += str(i[1])  #遍历将按照key值排序后的value值依次添加到字符串
        self.sign = self.get_md5(self.str)
        self.pubparam['sign'] = self.sign


    def get_rand_string(self,randomlength=22):
        '''生成随机字符串'''
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            str += chars[random.randint(0, length)]

        return str


    def send(self):
        r = requests.get(self.url,self.pubparam)  #实例化带pubparam参数的get请求

        if str(r.status_code) == '200':
            return r.status_code,r.json()
        else:
            return r.status_code
    def get_md5(self,string):
        m = hashlib.md5()  #生成一个md5 hash对象
        m.update(string.encode('utf-8'))  #生成hash对象后，用update方法对字符串进行md5加密的更新处理
        md5str = m.hexdigest()  #16进制的加密结果字符串
        return md5str

if __name__ == '__main__':
    key = {'userPhone':18380805107,'thirdType':'WX','openid':15}
    request2jvv('thirdBinding',key).send()