# 通过占位的形式，完成拼接
name = "lsy"
message = "%s月入1800，每天笑哈哈" % name
print(message)

# 快速占位 f是format的意思
salary = 1800
message = f"{name}月入{salary}"
print(message)

# 通过占位的形式，完成数字和字符串的拼接
salary = 1800
message = "%s月入%s，每天笑哈哈" % (name, salary)
print(message)

# %s 将内容转换成字符串，放入占位位置
# %d 转换成整数
# %f 转换成浮点型

year = 2023
tax = 47.56
message = "%s, %d, %f" % (name, year, tax)
print(message)