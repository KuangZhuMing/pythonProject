with open('user.txt') as user:
    #USER = user.read()
    #print(USER.rstrip()) #去除后面的换行

    USER = user.readlines()
# print(type(USER)) #列表
# for line in USER:
#     print(line.rstrip())

pi_string = '' #字符串存储
for line in USER:
    pi_string += line.rstrip() + ','
print(pi_string)
print(len(pi_string),type(pi_string))

#使用方法replace() 将字符串中的特定单词都替换为另一个单词


