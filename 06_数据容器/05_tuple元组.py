# 定义元组
t1 = (1, 'lsy', True)
t2 = ()
t3 = tuple()
print(t1, t2, t3)
print(type(t1), type(t2), type(t3))

# 定义单个元素的元组
t4 = ('lsy') # 是一个字符串，应该加一个,
print(t4, type(t4))
t4 = ('lsy',)
print(t4, type(t4))

# 元组的嵌套
t5 = ('lsy', ('lsy', '1'))
print(t5, type(t5))

# 下标索引去取出内容
print(t5[1][1])

# 元组的操作：index查找
# 元组的操作：count计算元素个数
# 元组的操作：len()元组元素个数

