# coding:utf-8
import os,configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path,"cfg.ini")
conf = configparser.ConfigParser()
conf.read(configPath,encoding='UTF-8')

# 服务器配置
eme = "test"
host_ip = conf.get(eme,"host_ip")
host_port = conf.get(eme,"host_port")
host_ues = conf.get(eme,"host_use")
host_pwd = conf.get(eme,"host_pwd")