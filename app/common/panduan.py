# -*- coding: utf-8 -*-
# @Date    : 2017-08-02 21:54:08
# @Author  : lileilei

def assert_in(asserqiwang,fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1=([(str(fanhuijson[key])) for key in result.keys()])
        value2=([(str(value)) for value in result.values()])
        if value1==value2:
            return  'pass'
        else:
            return 'fail'
    else:
        raise (u'请填写期望值')
def assertre(asserqingwang):
    if len(asserqingwang.split('=')) > 1:
        data = asserqingwang.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        LOG.info(u'填写测试预期值')
        raise (u'请填写期望值')

