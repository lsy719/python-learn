# 定义一个列表list 类似不受限制
my_list = ['123', '456', '789']

print(my_list)
print(type(my_list))

my_list = ['lsy', 123, True]
print(my_list)
print(type(my_list))

# 定义一个嵌套的列表
my_list = [1, [1, 2, 3]]
print(my_list)

print(my_list[1])
print(my_list[1][2])
print(my_list[1][-2])

my_list = ['123', '456', '789', 'lsy']
print(my_list[-1])
print(my_list[-3])