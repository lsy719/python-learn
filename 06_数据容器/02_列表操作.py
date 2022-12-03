# 列表的方法
# 插入元素
# 删除元素
# 清空列表
# 修改元素
# 统计元素个数

# 1.append() ——向列表的尾部添加元素
# 2.insert(index, object) ——向指定的下标处添加元素
# 3.sort() ——int类型从大到小 字母ASCII码
# 4.index() ——返回的是元素在列表中的第一个位置
# 5.reverse() ——将列表进行翻转
# 6.remove() ——删除某个元素，如果有重复，删除的是第一次出现的元素，如果元素不存在会报错
# 7.count() ——返回的是某个元素在列表里面的个数
# 8.clear() ——清除元素
# 9.copy() ——浅拷贝对象 不等价于 =
# 10.extend() ——合并列表
# 11.pop() ——删除列表尾部的元素，返回删除的元素

my_list = ['l', 's', 'y']
my_list.append('s')
print(my_list)

my_list.insert(1,'l')
print(my_list)


list1 = [1, 3, 5, 2, 4]
# 改变了原列表
list1.sort()
print(list1)

list1.reverse()
print(list1)

# 只能传一个参数
my_list.remove('l')
print(my_list)

print(my_list.count('s'))

# 浅复制
list2 = list1.copy()
list1.remove(1)
print(list1)

list1.clear()
print(list1)

print(list2)

my_list.extend(list2)
print(my_list, list2)

my_list.pop()
print(my_list)

