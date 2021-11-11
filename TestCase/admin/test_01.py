# -*- coding: utf-8 -*-

import allure
import pytest

from Params.params import admin
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestJYGK:

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('info')
    def test_01(self, action):
        """
            用例描述：用户详情
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[0]
        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('amount')
    def test_02(self, action):
        """
            用例描述：今日订单总额
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[1]
        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('orders')
    def test_03(self, action):
        """
            用例描述：支付数据
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[2]
        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('products_sales')
    def test_04(self, action):
        """
            用例描述：销售榜
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[3]
        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')