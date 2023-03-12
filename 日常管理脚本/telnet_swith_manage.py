import telnetlib
import time

user = "ytnet" #input("请输入用户名： ")
password = "ytnet123" #input("请输入密码 ")

for i in range(20,21):
    host='172.16.1.'+str(i)
    tn=telnetlib.Telnet(host)
    tn.read_until(b'Username:')
    tn.write(user.encode('ascii')+b'\n')
    tn.read_until(b'Password:')
    tn.write(password.encode('ascii')+b'\n')
    tn.write(b'sys\n')
    tn.write(b'display ip interface brief\n')
    command = "sysname huiz-sw-" + str(i) #修改设备名称命令，以IP地址结尾
    tn.write(command.encode('ascii')+b"\n")
    tn.write(b'return\n')
    tn.write(b'save\n')
    tn.write(b'y\n')
    tn.write(b'dis stp | include CIST Global Info\n')
    time.sleep(1)
    output=tn.read_very_eager().decode('ascii')
    print(output)
    tn.close()