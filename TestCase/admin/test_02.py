# -*- coding: utf-8 -*-

import allure
import pytest

from Params.params import admin
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestZLGL:

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('margin')
    def test_01(self, action):
        """
            用例描述：主营类目
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[4]
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
            用例描述：商家审核状态
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[5]
        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('seller')
    def test_03(self, action):
        """
            用例描述：买手列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[6]
        response = request.get_request(api_url)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('settled')
    def test_04(self, action):
        """
            用例描述：商家列表
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url
        data = data.data[7]
        api_url = host + urls[7]

        response = request.get_request(api_url,data)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('edit')
    def test_05(self, action):
        """
            用例描述：编辑商家资料
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0], action[1])

        host = conf.host_debug
        urls = data.url
        data = data.data[8]
        api_url = host + urls[8]

        response = request.put_request(api_url, data)

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('edit')
    def test_06(self, action):
        """
            用例描述：编辑商家资料
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0], action[1])

        host = conf.host_debug
        urls = data.url
        data = data.data[8]
        api_url = host + urls[8]

        response = request.put_request(api_url, data)

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')


    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('reject')
    def test_07(self, action):
        """
            用例描述：驳回商家资料
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0], action[1])

        host = conf.host_debug
        urls = data.url
        data = data.data[9]
        api_url = host + urls[9]

        response = request.put_request(api_url, data)

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'审批已通过，不可审批')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('pass')
    def test_08(self, action):
        """
            用例描述：通过商家资料
        """
        conf = Config()
        data = admin()
        test = Assert.Assertions()
        request = Request.Request(action[0], action[1])

        host = conf.host_debug
        urls = data.url
        data = data.data[10]
        api_url = host + urls[10]

        response = request.put_request(api_url, data)

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'审批已通过，不可审批')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

