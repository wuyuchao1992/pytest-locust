# -*- coding: utf-8 -*-

"""
封装request

"""

import os,json,urllib3
import random
import requests
import Common.Consts
from Common import Session,Hash
from requests_toolbelt import MultipartEncoder

# 控制台去除安全警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Request:

    def __init__(self, env,side):
        """
        :param env:
        """
        self.session = Session.Session()
        self.get_session = self.session.get_session(env,side)
        if self.get_session == None :
            print("session is None")
        else:
            self.headers = self.get_session

    def get_request(self, url, data=""):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """

        if self.get_session == None :
            print("session is None")
            return None
        else:
            try:
                loginData = {}
                loginData.update(data)
                response = requests.get(url=url, data=data,headers = self.headers,verify=False)
            except requests.RequestException as e:
                print('%s%s' % ('RequestException url: ', url))
                print(e)
                return ()

            except Exception as e:
                print('%s%s' % ('Exception url: ', url))
                print(e)
                return ()

            time_consuming = response.elapsed.microseconds/1000
            time_total = response.elapsed.total_seconds()

            Common.Consts.STRESS_LIST.append(time_consuming)

            response_dicts = dict()
            response_dicts['code'] = response.status_code
            try:
                response_dicts['body'] = response.json()
            except Exception as e:
                print(e)
                response_dicts['body'] = ''
            response_dicts['text'] = response.text
            response_dicts['time_consuming'] = time_consuming
            response_dicts['time_total'] = time_total

            return response_dicts

    def post_request(self, url, data):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """

        if self.get_session == None:
            print("session is None stop request")

        else:
            try:
                loginData = {}
                loginData.update(data)
                response = requests.post(url=url, json=loginData,headers = self.headers,verify=False)
            except requests.RequestException as e:
                print('%s%s' % ('RequestException url: ', url))
                print(e)
                return ()

            except Exception as e:
                print('%s%s' % ('Exception url: ', url))
                print(e)
                return ()

            # time_consuming为响应时间，单位为毫秒
            time_consuming = response.elapsed.microseconds/1000
            # time_total为响应时间，单位为秒
            time_total = response.elapsed.total_seconds()

            Common.Consts.STRESS_LIST.append(time_consuming)

            response_dicts = dict()
            response_dicts['code'] = response.status_code
            try:
                response_dicts['body'] = response.json()
            except Exception as e:
                print(e)
                response_dicts['body'] = ''

            response_dicts['text'] = response.text
            response_dicts['time_consuming'] = time_consuming
            response_dicts['time_total'] = time_total

            return response_dicts

    def post_request_multipart(self, url, data, header, file_parm, file, f_type):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header, cookies=self.get_session)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, params=data, headers=header, cookies=self.get_session)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_request(self, url, data=''):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if self.get_session == None:
            print("session is None stop request")

        try:
            if data is None:
                response = requests.put(url=url, headers=self.headers, verify=False)
            else:

                response = requests.put(url=url, json=data, headers=self.headers,verify=False)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_request_uploadFiles(self, url, file_parm, file, f_type):
        """
        提交File格式的Post请求
        :param url:
        :param file_parm:文件参数
        :param file:文件地址
        :param type:
        :return:
        """

        try:
            data = {}
            data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

            response = requests.post(url=url, files=data)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_request_noToken(self, url, data):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:

        """

        try:

            response = requests.post(url=url, json=data,verify=False)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

