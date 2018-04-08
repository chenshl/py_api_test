#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author   : csl
# @Time    : 2017/3/17 11:02
import unittest
from common.request2jvv import request2jvv
class userResetPwd(unittest.TestCase):
    '''重置用户登录、交易密码'''  #测试组备注
    def setUp(self):
        self.service = 'userResetPwd'
    def tearDown(self):
        pass

    def test_suc_resetloginpwd(self):
        '''正确重置登录密码'''  #测试组中的单个测试方法备注
        self.param = {'userId':'201703010010000000457',
                      'realname':'',
                      'idcard':'',
                      'pwdType':'0'}

        r = request2jvv(self.service,self.param).send()
        print(r)

if __name__ == '__main__':
    unittest.main()