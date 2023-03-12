import paramiko
import time

log_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
user = input("username:")
password = input("password:")
f = open("ip_list.txt", "r")
for line in f.readlines():
    ip = line.strip()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip,username=user,password=password) #ssh远程登录
    print(log_time + " 成功连接交换机，开始巡检 " + ip)
    command = ssh.invoke_shell() #用于创建一个子shell进程
    command.send("system\n")
    command.send("display ip routing-table\n")
    command.send("display device\n")
    command.send("display environment\n")
    command.send("display alarm urgen\n")
    command.send("display memory-usage\n")

    command.send("display version\n")
    command.send("display fan \n")
    f = open("check.txt", "a") #这a代表写入，不能用w，w是直接叠加会将之前写入的数据清理。
    time.sleep(2)
    output = command.recv(65535) #返回结果字符为65535
    result = output.decode("ascii")
    f.write(result)
    print(result)
    f.close()
ssh.close()
