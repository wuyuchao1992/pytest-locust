import hashlib,time,unittest,requests,json,uuid
import time,threading,pymysql
import datetime
import paramiko, getpass  # getpass是隐藏密码
# 获取时间戳并去除小数点
ticks = str(time.time()).replace('.','')
timestamp = ticks[:-4]
# 账号密码
account = "15976427940"
password = "c4ca4238a0b923820dcc509a6f75849b"

class base():
    # 参数按键盘排序,用&拼接起来再MD5加密
    def encrypt(self, params, salt='DFHGKZLSE2NFDEHGFHHR4XTGBKHY67EJZ8IK9'):
        # 排序
        keys = params.keys()
        tmp_list = []
        for item in keys:
            tmp_list.append(item)
        tmp_list.sort()
        tmp_content = ''
        for item in tmp_list:
            tmp_content += item + '=' + str(params[item]) + '&'
        string =  tmp_content[:-1]
        # MD5加密
        string = string + salt
        m = hashlib.md5()
        m.update(string.encode(encoding="utf-8"))
        return m.hexdigest()

    def signSort(self, params):
        # 排序
        keys = params.keys()
        tmp_list = []
        for item in keys:
            tmp_list.append(item)
        tmp_list.sort()
        tmp_content = ''
        for item in tmp_list:
            tmp_content += item + '=' + str(params[item]) + '&'
        string =  tmp_content[:-1]
        return string

    def Caltime(self,date1,date2):
        # %Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
        # date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
        # date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
        date01 = time.strptime(date1, "%Y-%m-%d")
        date02 = time.strptime(date2, "%Y-%m-%d")
        # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
        # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
        # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
        date03 = datetime.datetime(date01[0], date01[1], date01[2])
        date04 = datetime.datetime(date02[0], date02[1], date02[2])
        # 返回两个变量相差的值，就是相差天数
        return date04 - date03

    def getTwoFloat(self,f_str, n):
        f_str = str(f_str)  # f_str = '{}'.format(f_str) 也可以转换为字符串
        a, b, c = f_str.partition('.')
        c = (c + "0" * n)[:n]  # 如论传入的函数有几位小数，在字符串后面都添加n为小数0
        return ".".join([a, c])

    # 生成唯一UUID
    def create_uid(self):
        return str(uuid.uuid1())

    def get_timestamp(self):
        timestamp = (str(time.time()).replace('.', ''))[:-4]
        return timestamp

    def md5(self,string):
        string = str(string)
        m =hashlib.md5(string.encode(encoding='UTF-8')).hexdigest()
        return m


    def ssh_connect(self,host_ip,host_port,host_use,host_pwd,command):

        # # 待执行的命令
        # sed_command = "./easyNmon"
        # ls_command = "lsof - i: 9999"
        #
        # # 注意：依次执行多条命令时，命令之间用分号隔开
        # command = sed_command + ";" + ls_command
        # SSH远程连接
        ssh = paramiko.SSHClient()  # 创建sshclient
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())  # 指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
        ssh.connect(hostname=host_ip,port=host_port,username=host_use,password=host_pwd)

        # 执行命令并获取执行结果
        stdin, stdout, stderr = ssh.exec_command(command)
        out = stdout.readlines()
        err = stderr.readlines()

        ssh.close()
        print(out,err)

    def selcetSQL(self,sql):
        # 连接数据库
        hostvalue ="106.55.94.254"
        uservalue = "root"
        passwordvalue = "root"
        dbvalue = "choujiang"
        portvalue = 3306
        connection = pymysql.connect(host=hostvalue, user=uservalue, password=passwordvalue, db=dbvalue,
                             port=portvalue, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        cursor = connection.cursor()
        # 创建sql 语句,并执行
        sqlvalue = sql  # "select * from user"
        cursor.execute(sqlvalue)
        result = cursor.fetchone()  # 查询数据库单条数据
        # result = cursor.fetchall() #查询数据库多条数据
        cursor.close()
        return result

if __name__ == "__main__":
    import random
    b = base()
    mobile = 15976427940
    code =  (b.selcetSQL("SELECT verifyCode FROM choujiang.user u WHERE mobile=%i"%mobile))["verifyCode"]
    print(code)