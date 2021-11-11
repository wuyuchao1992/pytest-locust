# -*- coding: utf-8 -*-

import allure,random
import pytest

from Params.params import shop
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestReg:


    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('statistics')
    def test_01(self, action):
        """
            用例描述：订单统计
        """
        conf = Config()
        data = shop()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[13]

        response = request.get_request(api_url)

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('orders')
    def test_02(self, action):
        """
            用例描述：订单列表
        """
        conf = Config()
        data = shop()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[14]

        response = request.get_request(api_url)

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')