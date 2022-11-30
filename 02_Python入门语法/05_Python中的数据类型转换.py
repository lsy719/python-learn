# 将数字类型转换成字符串
# 任何类型都能通过str转换成字符串
num_str = str(111)
print(type(num_str), num_str)
float_str = str(12.12)
print(type(float_str), float_str)

# 将字符串转换成数字
num = int("11")
print(type(num), num)
num2 = float("11.11")
print(type(num2), num2)
# 字符串转数字，必须内容是数字
# print(type(int("lsy")))

# 整数转浮点数
print(type(float(11)), float(11))

# 浮点数转整数(丢失精度)
print(type(int(12.34)), int(12.34))
