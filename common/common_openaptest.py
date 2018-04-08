#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : csl
# @Time   : 2017/3/17 11:17
'''用于openapi单个接口调试用'''
from common.request2jvv import request2jvv
from common.writelog import writelog
def openapitest():
    servicename = input('请输入接口名(exit0表示退出)：')
    if servicename == 'exit0':
        exit()
    else:
        writelog('info', '==============')
        writelog('info', '接口名：%s' % servicename)
        param = (input('请输入参数名（a=xx;b=xx）:'))
        writelog('info', '参数：%s' % param)
        paramlist = param.split(';')  #输入的字符串分割为列表
        paramdict = {}
        for i in paramlist:
            paramdict[i.split('=')[0]] = i.split('=')[1]  #分割后的列表转换为字典
        try:
            r = request2jvv(servicename,paramdict).send()
            if len(r) == 1:  #r为响应内容，返回数组格式还是字典还是json？
                print('响应状态码:%s' % str(r))
            else:
                print('响应状态码:%s' % str(r[0]))
                print('响应报文:%s' % r[1])
            writelog('info','相应报文：%s' % str(r))
        except BaseException as e:
            writelog('info','响应异常：%s' % e)  #抛出具体异常
        finally:
            writelog('info', '==============')
            openapitest()  #如果抛错程序不终止，一直执行此方法



if __name__ == '__main__':
    openapitest()