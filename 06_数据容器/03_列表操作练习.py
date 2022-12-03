# 有一个列表，内容是：[21, 25, 21, 23, 22, 20]

# 1.定义这个列表
# 2.追加一个数字31，到列表的尾部
# 3.追加一个新列表[29, 33, 30]，到列表的尾部
# 4.取出第一个元素 21
# 5.取出最后一个元素
# 6.查找元素31下表

list1 = [21, 25, 21, 23, 22, 20]
print(list1)
list1.append(31)
print(list1)
list2 = [29, 33, 30]
list1.extend(list2)
print(list1)
print(list1[0])
print(list1[-1])
print(list1.index(31))
