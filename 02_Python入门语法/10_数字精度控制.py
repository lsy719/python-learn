num1 = 22
num2 = 12.345
print("%5d" % num1)
# [空格][空格][空格] 22

# 宽度如果比本身小，相当于没写，浮点数宽度包括整数部分 + 小数点 + 小数部分
print("%4.2f" % num2)
print("%7.2f" % num2)

print("%.1f" % num2)
