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
    @allure.story('register')

    def test_01(self, action):
        """
            用例描述：获取注册验证码
        """
        conf = Config()
        data = shop()
        test = Assert.Assertions()
        request = Request.Request(action[0],action[1])

        host = conf.host_debug
        urls = data.url

        api_url = host + urls[0]

        phone = random.randint(1000, 9999) + 19367890000

        # 获取验证码
        response = request.post_request_noToken(api_url,{"phone":phone})
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'发送验证码成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

        api_url = host + urls[1]

        # 校验获取验证码
        response = request.post_request_noToken(api_url,{"phone":phone,"smsCode":"1234"})
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'校验成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

        api_url = host + urls[2]
        data = data.data[2]

        # 更新参数
        data["phone"] = phone

        # 注册
        response = request.post_request_noToken(api_url,data)
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'msg', u'提交成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')