# -*- coding: utf-8 -*-

"""
封装获取cookie方法

"""

import requests,json,urllib3

from Common import Log,Hash
from Conf import Config


class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def get_session(self, env,side):
        """
        获取session
        :param env: 环境变量
        :param side: 后台变量
        :return:
        """
        if env == "test" and side == "admin":
            self.login_url = self.config.admin_loginHost_debug
            self.parm = json.loads(self.config.admin_loginInfo_debug)
            self.path = self.config.host_debug

        elif env == "gray" and side == "admin":
            self.login_url = self.config.admin_loginHost_release
            self.parm = json.loads(self.config.admin_loginInfo_release)
            self.path = self.config.host_release

        elif env == "test" and side == "shop":
            self.login_url = self.config.shop_loginHost_debug
            self.parm = json.loads(self.config.shop_loginInfo_debug)
            self.path = self.config.host_debug

        elif env == "gray" and side == "shop":
            self.login_url = self.config.shop_loginHost_release
            self.parm = json.loads(self.config.shop_loginInfo_release)
            self.path = self.config.host_release

        # 控制台去除安全警告
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        getcodeUrl = self.path + "/api/v1/pb/auz/open/login/verify/img/code"
        params = {"mobile":self.parm["mobile"]}
        getcode = requests.post(getcodeUrl,params,verify=False)

        if getcode.status_code == 200:
            session_debug = requests.session()
            response = session_debug.post(self.login_url, self.parm,verify=False)
            if response.status_code == 200:
                if response.json()["code"] == 200:
                    token = response.json()["data"]["value"]
                    type = response.json()["data"]["tokenType"]
                    self.headers = {"Authorization":type + " " + token}
                    return self.headers
                else:
                    self.log.error('get cookies error, please checkout!!!')
                    return None

            else:
                token = response.text
                print(token)
                print("get cookies error")
                self.log.error('get cookies error, please checkout!!!')
                return None

        else:
            print("get code error")


if __name__ == '__main__':
    ss = Session()
    s = ss.get_session('test',"shop")
    print(s)