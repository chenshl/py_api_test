#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : csl
# @Time    : 2017/3/14 14:32
import requests
class request2jww(object):
    global apiHeader  #全局变量
    apiHeader = 'http://192.168.1.8:9999'
    def __init__(self,apiName='',apiParam = {}):
        self.apiName = apiName
        self.apiParam = apiParam
        # self.send()

    def get_fullAPIUrl(self,apiName):
        return apiHeader + apiName  #拼接完整接口地址

    def send(self):
        self.sortapiParam = self.sortParam()
        r = requests.post(self.get_fullAPIUrl(self.apiName),self.sortapiParam)  #实例化post请求
        if r.status_code == 200:
            self.body = r.json()  #请求结果转换为json格式
            if self.body['result'] == str(1):
                print(self.body)
            else:
                print('请求失败')
        return self.body
    def sortParam(self):
        # sorted(self.apiParam.items())
        # for k,v in self.apiParam.items():
        #     if v is None:
        #         return False
        # return True
        return sorted(self.apiParam.items())  #参数按照key值排序

if __name__ == '__main__':
    # apiname = '/s/shop/pay/wobi/qry'
    # apiParam = {'userId':'000065bc-bcb2-11e5-b300-d89d672713e0'}
    # request2jww(apiName=apiname,apiParam=apiParam).send()

    # apiname = "/s/web/login"
    # apiParam = {"mobile":"18716200002",
    #             "loginpwd":"111111",
    #             "appName":"ohmyjvv_logintokenCq"}

    apiname = "/m/getUserInfoByToken"
    apiParam = {"token": "d145131e2bddd4817b297cb5329e35bc",
                "appName": "ohmyjvv_logintokenCq"}
    request2jww(apiName=apiname, apiParam=apiParam).send()