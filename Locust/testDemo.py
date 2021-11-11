# ！/usr/bin/env python
# -*- coding:utf-8 -*-

import queue,json,random,time
from locust import HttpUser,task,SequentialTaskSet,constant,between

class reg(SequentialTaskSet):

    # 公共方法
    def post(self, path, params, headers=''):
        with self.client.post(url=path, data=params, headers=headers,
                              catch_response=True) as self.response:  # catch_response值为布尔类型，如果设置为 True, 允许该请求被标记为失败
            if self.response.status_code == 200:

                # if json.loads(self.response.text)["code"] == 1:
                self.response.success()  # 标记请求成功
            # else:
            #     self.response.failure('Failed!')  # 标记请求失败
            #     print(self.response.text)
            else:
                self.response.failure('Failed!')  # 标记请求失败
                print(self.response.text)
                return None
    def get(self, path, headers):
        with self.client.get(url=path, name=path, headers=headers,
                             catch_response=True) as self.response:  # catch_response值为布尔类型，如果设置为 True, 允许该请求被标记为失败
            if self.response.status_code == 200:
                if json.loads(self.response.text)["code"] == 1:
                    # print(json.loads(response.text)["data"]["qr_code"])
                    self.response.success()  # 标记请求成功
                else:
                    self.response.success()  # 标记请求成功
                    print(self.response.text)
                    return None
            else:
                self.response.failure('Failed!')  # 标记请求失败
                print(self.response.text)
                return None

    user_data_queue = queue.Queue()
    for index in range(400):
        data = 19267890001+index
        user_data_queue.put_nowait(data)

    @task
    def reg(self):
        path = "/Api/Index/reg"
        params = {"username":self.user_data_queue.get(),
                  "verify_code":"99999999",
                  "password":"a123456",
                  "type":"1",
                  "login_platform":"app",
                  "invite_code":"CG6691332"}
        self.post(path=path,params=params)

class live(SequentialTaskSet):

    # 公共方法
    def post(self, path, params, headers):
        with self.client.post(url=path, data=params, headers=headers,
                              catch_response=True) as self.response:  # catch_response值为布尔类型，如果设置为 True, 允许该请求被标记为失败
            if self.response.status_code == 200:

                # if json.loads(self.response.text)["code"] == 1:
                self.response.success()  # 标记请求成功
            # else:
            #     self.response.failure('Failed!')  # 标记请求失败
            #     print(self.response.text)
            else:
                self.response.failure('Failed!')  # 标记请求失败
                print(self.response.text)
                return None
    def get(self, path, headers):
        with self.client.get(url=path, name=path, headers=headers,
                             catch_response=True) as self.response:  # catch_response值为布尔类型，如果设置为 True, 允许该请求被标记为失败
            if self.response.status_code == 200:
                if json.loads(self.response.text)["code"] == 1:
                    # print(json.loads(response.text)["data"]["qr_code"])
                    self.response.success()  # 标记请求成功
                else:
                    self.response.success()  # 标记请求成功
                    print(self.response.text)
                    return None
            else:
                self.response.failure('Failed!')  # 标记请求失败
                print(self.response.text)
                return None

    user_data_queue = queue.Queue()
    for index in range(400):
        data = 19267890001+index
        user_data_queue.put_nowait(data)
    def on_start(self):
        try:
            data = self.user_data_queue.get()
            url = "/Api/Index/login"
            params = {"username":data,"password":"a123456","type":"2"}
            with self.client.post(url=url, data=params,catch_response=True) as response:  # catch_response值为布尔类型，如果设置为 True, 允许该请求被标记为失败
                if response.status_code == 200:
                    if json.loads(response.text)["code"] == 1:
                        response.success()  # 标记请求成功
                        token = json.loads(response.text)["data"]["token"]
                        nickname = json.loads(response.text)["data"]["nickname"]
                        self.headers = {"access-token": token,"Content-Type": "application/x-www-form-urlencoded","Device-Type":"5","phone":nickname,}
                        return self.headers
                    else:
                        response.failure('Failed!')  # 标记请求失败
                        print(response.text,url)
                        return None
                else:
                    response.failure('Failed!')  # 标记请求失败
                    print(response.status_code)
                    return None
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)

    # 直播用例
    l_id = 493

    @task(1)
    def live_takeGoods(self):
        self.post(path="/Api/Live/takeGoods", params={"page": 1, "l_id": self.l_id, "keyword": "", "platform": "live"},
                  headers=self.headers)

    @task(2)
    def live_detail(self):
        self.post(path="/Api/Live/detail", params={"l_id": self.l_id, "invite_code": "CG9473965", "platform": "live"},
                  headers=self.headers)

    @task
    def share_poster(self):
        self.post(path="/Api/Live/sharePoster",params={"l_id":self.l_id,"platform":"live"},headers=self.headers)

    @task
    def get_ShareInfo(self):
        self.post(path="/Api/Goods/getShareInfo",params={"goods_id":19507,"type":1,"related_id":self.l_id,"is_share":0,"platform":"live"},headers=self.headers)

    @task
    def share_goodsList(self):
        self.get(path="/index.php/openmall/share/goodsList?platform=openmall",headers=self.headers)
        if json.loads(self.response.text)["data"]["qr_code"] == '':
            print(json.loads(self.response.text)["data"]["qr_code"])
            self.response.failure('Failed!')
        # else:
        #     print("【"+json.loads(self.response.text)["data"]["qr_code"] + "】" + "【" + str(self.headers) + "】")

    @task
    def good_detail(self):
        self.post(path="/index.php/openmall/goods/detail",params={"goods_id":"28957","platform":"openmall"},headers=self.headers)
        if json.loads(self.response.text)["data"]["qr_code"] == '':
            print(json.loads(self.response.text)["data"]["qr_code"])
            self.response.failure('Failed!')
        # else:
        #     print("【"+json.loads(self.response.text)["data"]["qr_code"] + "】" + "【" + str(self.headers) + "】")

class submitOrder(SequentialTaskSet):

    # 公共方法
    def post(self, path, params, headers):
        with self.client.post(url=path, data=params, headers=headers,
                              catch_response=True) as self.response:  # catch_response值为布尔类型，如果设置为 True, 允许该请求被标记为失败
            if self.response.status_code == 200:

                # if json.loads(self.response.text)["code"] == 1:
                self.response.success()  # 标记请求成功
            # else:
            #     self.response.failure('Failed!')  # 标记请求失败
            #     print(self.response.text)
            else:
                self.response.failure('Failed!')  # 标记请求失败
                print(self.response.text)
                return None
    def get(self, path, headers):
        with self.client.get(url=path, name=path, headers=headers,
                             catch_response=True) as self.response:  # catch_response值为布尔类型，如果设置为 True, 允许该请求被标记为失败
            if self.response.status_code == 200:
                if json.loads(self.response.text)["code"] == 1:
                    # print(json.loads(response.text)["data"]["qr_code"])
                    self.response.success()  # 标记请求成功
                else:
                    self.response.success()  # 标记请求成功
                    print(self.response.text)
                    return None
            else:
                self.response.failure('Failed!')  # 标记请求失败
                print(self.response.text)
                return None

    # 定义队列
    user_data_queue = queue.Queue()

    # 在队列存放参数
    for index in range(400):
        data = 19267890001+index
        user_data_queue.put_nowait(data)

    # 每次请求前都要根据队列参数进行登录
    # 登录用户数与运行 -u -r 配置相关
    def on_start(self):
        try:
            data = self.user_data_queue.get()
            url = "/Api/Index/login"
            params = {"username":"13427505064","password":"a123456","type":"2"}
            with self.client.post(url=url, data=params,catch_response=True) as response:  # catch_response值为布尔类型，如果设置为 True, 允许该请求被标记为失败
                if response.status_code == 200:
                    if json.loads(response.text)["code"] == 1:
                        response.success()  # 标记请求成功
                        token = json.loads(response.text)["data"]["token"]
                        nickname = json.loads(response.text)["data"]["nickname"]
                        self.headers = {"access-token": token,"Content-Type": "application/x-www-form-urlencoded","Device-Type":"5","phone":nickname,}
                        return self.headers
                    else:
                        response.failure('Failed!')  # 标记请求失败
                        print(response.text,url)
                        return None
                else:
                    response.failure('Failed!')  # 标记请求失败
                    print(response.status_code)
                    return None
        except queue.Empty:
            print('account data run out, test ended.')
            exit(0)

    @task
    def addAddress(self):
        # 新增地址
        # print(self.headers)
        self.post(path="/Api/User/addAddress",params={"consignee":"TESTER","province":"1","city":"2","district":"3","address":"TEST_ADDRESS","mobile":"18888888888"},headers=self.headers)

    @task
    def addressList(self):
        # 获取地址列表
        self.get(path="/Api/User/addressList",headers=self.headers)
        self.addressId = json.loads(self.response.text)["data"]["data"][0]["address_id"]

    @task
    def submitOrder(self):
        # 提交订单
        self.post(path="/Api/Cart/submitOrder",params={"address_id":self.addressId,"act":"submit_order","goods_id":"19940","goods_num":"1","source":"2","item_id":"","prom_type":"0","prom_id":"0"},headers=self.headers)
        if json.loads(self.response.text)["code"] !=1:
            print(json.loads(self.response.text))
        else:
            orderId = json.loads(self.response.text)["data"]["order_id"]

            # 虚拟支付
            self.post(path="/Api/Index/testpay",params={"order_id":orderId,"extension_code":"02020100722001433940"+str(random.randint(1,90000000000)+99999999)},headers=self.headers)

# 继承 httpUser
class cnblogUser(HttpUser):
    host = "https://test-lives-api.chungoulife.com"
    tasks = [reg]
    wait_time = between(0,0)

if __name__ == '__main__':
    import os
    os.system("locust -f testDemo.py --headless -u 100 -r 50 --run-time 60s")