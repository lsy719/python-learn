my_list = [0, 1, 2, 3, 4, 5, 6]

# 序列[起始下标:结束下标:步长]
# 起始下标可以留空，视作从头开始
# 结束下标可以留空，视作截取到末尾
# 步长1 一个个取， 步长N， 隔N-1个
# 步长为负数，反向取，起始和结束下标也要反向
my_str = '现在是，幻想时间'
my_str_list = []
for elem in my_str:
    my_str_list.append(elem)

print(my_str_list[4::])



