# 对文件的相关操作
#打开文件获得文件对象
# f = open("E:/Python.txt","r",encoding="UTF_8")
#文件对象的读取，不指定长度默认全部读取,文件的读取是顺序进行的，下一次的读取会以上一次读取的末尾为起始位置
# content = f.read(20)
# content_2 = f.read()
# print(content)
# print(content_2)
#读取一行文件
# content = f.readline()
# print(content)
#读取所有行文件,并存放在列表中
# list = f.readlines()
# print(list)
#for循环遍历文件的所有行，得到每行的数据
# for line in f:
#     print(line)
#关闭文件的对象,如果文件足够大，读取完毕不及时，则需要关闭文件
# f.close()
#通过with open语法打开文件，可以自动关闭
# with open("E:/Python.txt","r",encoding="UTF_8") as f:
#     for list_1 in f:
#         print(list_1)
#文件的写入操作
#文件的创建，文件不存在则创建文件，文件存在则清空文件再写入相关内容
# f = open("E:/Python2.txt","w",encoding="UTF_8")
#write()写函数，该函数可以实现写入内容
# f.write("黑马程序员")
#flush刷新，在写入内容后要刷新flush,才能写入文件
# f.flush()
#文件的关闭，在关闭文件的同时，同样具备刷新flash的功能
# f.close()
#文件的追加操作，当文件不存在时创建文件，当文件存在时继续追加文件内容,其它与文件的写入操作一模一样
# f = open("E:/Python2.txt","a",encoding="UTF_8")
#write()写函数，该函数可以实现写入内容
# f.write("777")
#flush刷新，在写入内容后要刷新flush,才能写入文件
# f.flush()
#文件的关闭，在关闭文件的同时，同样具备刷新flash的功能
# f.close()


