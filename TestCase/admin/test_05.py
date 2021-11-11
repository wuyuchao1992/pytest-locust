# -*- coding: utf-8 -*-

import allure
import pytest

from Params.params import admin
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert

class TestJSGL:

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('settlement')
    def test_01(self, action):
        """
            用例描述：结算列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[22]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('status')
    def test_02(self, action):
        """
            用例描述：订单状态
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[23]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('status')
    def test_03(self, action):
        """
            用例描述：结算状态
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[24]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('export')
    def test_04(self, action):
        """
            用例描述：导出结算列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[25]
        data = data.data[25]

        response = request.post_request(api_url,data)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('settlement')
    def test_05(self, action):
        """
            用例描述：提现管理列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[26]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('status')
    def test_06(self, action):
        """
            用例描述：银行卡账户类型
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[27]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('status')
    def test_07(self, action):
        """
            用例描述：结算审核状态
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[28]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('status')
    def test_08(self, action):
        """
            用例描述：提现状态
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[29]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('merchant')
    def test_09(self, action):
        """
            用例描述：银行卡列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[30]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('status')
    def test_10(self, action):
        """
            用例描述：银行卡状态
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[31]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('selection/status')
    def test_11(self, action):
        """
            用例描述：收支明细业务类型
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[31]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('settlement/trade')
    def test_12(self, action):
        """
            用例描述：收支明细列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[32]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('cards/merchant')
    def test_13(self, action):
        """
            用例描述：银行卡列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0] ,action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[33]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')