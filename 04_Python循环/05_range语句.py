# for 临时变量 in 待处理数据集:
# 循环满足条件时执行的代码
# 语法中的：待处理数据集，严格来说，称之为：序列类型
# Iteration 可以一个个依次取出的一种类型，报错字符串、列表、元组

# range(num)
# 获取一个从0开始，到num结束的数字序列（不含num本身）
print(range(3), type(range(3)))
for x in range(10):
    print(f"{x} ", end="")

# range(num1, num2)
# 获得一个从num1开始，到num2结束的数字序列（不包含num2本身）


# range(num1, num2, step)
# 获得一个从num1开始，到num2结束的数字序列（不包含num2本身）
# 数字之间的步长，以step为准（默认是1）
print()
import random
count = 0
res = random.randint(1, 100)
for x in range(1, res):
    if x % 2 == 1:
        count += 1
print(f"res = {res}, 有{count}个偶数")

