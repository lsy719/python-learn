# 无序(除非里面是int，会自动排序)、无重复、无法更改其中相符

# 定义集合
my_set = {'1', '2', '3'}

# 添加新元素
my_set.add('4')
my_set.update(['lsy','ysl'])

# 移除元素
my_set.remove('lsy')

# 随机取出一个元素

set1 = {1, 2, 3, 6}
set2 = {3, 4, 5}
set3 = {1, 2, 3, 4, 5}
# 清空集合

# 取2个集合的差集
set4 = set1.difference(set2)
print(set4)

# 消除2个集合的差集,此集合中不存在于其它指定集合中的项目
print(set1.difference_update(set3))

# 2个集合合并为1个
set3 = set1.union(set2)
print(set3)

# 统计集合元素数量

# 集合的遍历
for x in my_set:
    print(x) # 每次运行输出都不一样

# 清除集合
my_set.clear()
print(my_set)

# 彻底删除集合
del my_set