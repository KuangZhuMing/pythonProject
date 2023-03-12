filename = 'programming.txt'

# #定读取模式 读 （'r' ）、写入模式 写 （'w' ）、附加模式 附 （'a' ）或让你能够读取和写入文件的模式（'r+' ）
# with open(filename,'w') as file_object:
#     file_object.write("I love python\n")
#     file_object.write("I love creating ne gaems.\n")

with open(filename,'a') as file_object: #a追加模式
    file_object.write("I also love python\n")
    file_object.write("I love creating apps.\n")
