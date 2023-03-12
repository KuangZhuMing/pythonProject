# -*- coding: utf-8 -*-
from netmiko.huawei.huawei import HuaweiSSH
from netmiko import NetMikoTimeoutException
from netmiko import NetMikoAuthenticationException
from getpass import getpass
import re
import io
import xlwt


def main():
    """
        主函数
    """
    # 让用户输入ssh用户名密码
    username = input('请输入ssh用户名：')
    password = getpass('请输入ssh密码：')

    # 打开ip_list.txt文件获取IP列表
    ip_list = open('ip_list.txt', 'r')
    ip_addr = ip_list.readlines()
    ip_list.close()

    cmd_line = ['display version', 'display cpu-usage', 'display memory-usage', 'display device']

    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    # 初始化表格
    worksheet.write(0, 0, label="交换机IP")
    worksheet.write(0, 1, label="交换机名称")
    worksheet.write(0, 2, label="软件版本")
    worksheet.write(0, 3, label="CPU利用率")
    worksheet.write(0, 4, label="内存利用率")
    worksheet.write(0, 5, label="硬件状态")
    hang = 0
    lie = 0

    # 遍历ip列表用来生成迭代器
    for ip in iter(ip_addr):
        print(' ')
        print('本次巡检的设备IP：' + ip)
        try:
            S5720 = {
                'device_type': 'huawei',
                'ip': ip,
                'username': username,
                'password': password,
            }
            # 实例化HuaweiSSH
            net_connect = HuaweiSSH(**S5720)
            # print ("恭喜，成功登录")
            # print ("设备名：" + str(net_connect.find_prompt().strip('<>')))
            ip_str = (ip)
            hang = hang + 1
            # 初始化表格列
            lie = 0
            worksheet.write(hang, lie, label=ip_str)
            lie = lie + 1
            worksheet.write(hang,
                            lie,
                            label=net_connect.find_prompt().strip('<>'))
            for cmd in iter(cmd_line):
                cmd_result = net_connect.send_command(cmd)
                regex_str = []
                if 'VRP (R) software' in cmd_result:
                    regex_str = '\(\w*\d\d.*\)'
                    version = (re.search(regex_str, cmd_result))
                    lie = lie + 1
                    worksheet.write(hang,
                                    lie,
                                    label=version.group().strip('()'))
                    cmd_result = ''
                if 'CPU ' in cmd_result:
                    regex_str = '\d*.\d*.\%'
                    cpu_usage = (re.search(regex_str, cmd_result))
                    lie = lie + 1
                    worksheet.write(hang,
                                    lie,
                                    label=cpu_usage.group().strip(' '))
                    cmd_result = ''
                if 'Memory ' in cmd_result:
                    regex_str = '\d*.\%'
                    memory = (re.search(regex_str, cmd_result))
                    lie = lie + 1
                    worksheet.write(hang, lie, label=memory.group())
                    cmd_result = ''
                if 'Device ' in cmd_result:
                    if 'Abnormal' in cmd_result:
                        lie = lie + 1
                        worksheet.write(hang, lie, label=u"Abnormal")
                    elif 'WrongType' in cmd_result:
                        lie = lie + 1
                        worksheet.write(hang, lie, label=u"WrongType")
                    elif 'Unregistered' in cmd_result:
                        lie = lie + 1
                        worksheet.write(hang, lie, label=u"Unregistered")
                    elif 'Off' in cmd_result:
                        lie = lie + 1
                        worksheet.write(hang, lie, label=u"Off")
                    elif 'Offline' in cmd_result:
                        lie = lie + 1
                        worksheet.write(hang, lie, label=u"Offline")
                    else:
                        lie = lie + 1
                        worksheet.write(hang, lie, label=u"Normal")
                    cmd_result = ''

            net_connect.disconnect()
        except (EOFError, NetMikoTimeoutException):
            print('无法连接设备')
            netmikotimeout = (u'无法连接设备' + ip)
            hang = hang + 1
            lie = 0
            worksheet.write(hang, lie, label=netmikotimeout)
        except (EOFError, NetMikoAuthenticationException):
            print('用户名密码错误!')
            netmikotuehenticattion = (u'用户名密码错误' + ip)
            hang = hang + 1
            lie = 0
            worksheet.write(hang, lie, label=netmikotimeout)
        workbook.save('xunjian.xls')


if __name__ == '__main__':
    main()