# ！/usr/bin/env python
# -*- coding:utf-8 -*-

from locust import events
from locust.env import Environment
from locust.stats import stats_printer
from locust.runners import STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP, WorkerRunner
from locust.log import setup_logging, logging

import gevent
import time

from flask import request, Response
from locust import stats as locust_stats, runners as locust_runners
from locust import events
from prometheus_client import Metric, REGISTRY, exposition


import queue,json,random
from locust import HttpUser,task,SequentialTaskSet,constant,between

is_quitting = False

def checker(environment, ):

    """
    locust 退出时调用
    :param environment:
    :return:
    """

    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
    elif environment.stats.total.avg_response_time > 200:
        logging.error("Test failed due to average response time ratio > 200 ms")
        environment.process_exit_code = 1
    elif environment.stats.total.get_response_time_percentile(0.95) > 800:
        logging.error("Test failed due to 95th percentile response time > 800 ms")
        environment.process_exit_code = 1
    else:
        environment.process_exit_code = 0

@events.init.add_listener
def on_locust_init(environment, runner, **_kwargs):
    if not isinstance(environment.runner, WorkerRunner):
        gevent.spawn(checker, environment)


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

    # 队列生成账号
    user_data_queue = queue.Queue()
    for index in range(400):
        data = 19367890001+index
        user_data_queue.put_nowait(data)

    # 每次开始必执行方法，例如登录
    # 比如只登录100个账号，执行时设置100个user即可
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


class cnblogUser(HttpUser):
    host = "https://test-lives-api.chungoulife.com"
    tasks = [live]
    wait_time = between(1,2)
# setup Environment and Runner

env = Environment(user_classes=[cnblogUser])
env.create_local_runner()

# start a WebUI instance
env.create_web_ui("127.0.0.1", 8089)

# start a greenlet that periodically outputs the current stats
gevent.spawn(stats_printer(env.stats))

# start the test
env.runner.start(10, hatch_rate=10)

# in 60 seconds stop the runner
gevent.spawn_later(60, lambda: env.runner.quit())

# wait for the greenlets
env.runner.greenlet.join()

# stop the web server for good measures
env.web_ui.stop()