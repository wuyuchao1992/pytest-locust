# -*- coding: utf-8 -*-

import allure
import pytest

from Params.params import admin
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestBZJGL:

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('trade')
    def test_01(self, action):
        """
            用例描述：保证金管理列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[15]
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
            用例描述：交易类型
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[16]
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
            用例描述：交易状态
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[17]
        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('status')
    def test_04(self, action):
        """
            用例描述：支付方式
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[18]
        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('status')
    def test_05(self, action):
        """
            用例描述：支付方式
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url
        data = data.data[19]
        api_url = host + urls[19]

        response = request.post_request(api_url,data)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('category')
    def test_06(self, action):
        """
            用例描述：保证金配置列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[20]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('margin')
    def test_07(self, action):
        """
            用例描述：主营类目列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url
        api_url = host + urls[21]

        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')