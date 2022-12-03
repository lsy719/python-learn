my_str = ' CyberPunk 2077 '
# 字符串不支持修改
# 通过下标索引取值
print(my_str[2])
print(my_str[-4])

# index方法
print(my_str.index("C"))

# replace方法
# 将字符串的全部字符串1替换成字符串2, 不是修改本身，二十得到了一个新字符串
print(my_str.replace('7', '2'))

# split方法
# 得到一个列表，不改变原字符串
print(my_str.split(' '))

# strip方法
# 字符串的规整操作（去前后空格）
print(my_str.strip().split())
# 去指定字符串
print(my_str.strip().strip('7'))
# 1.字符串最后是空格不是7，所以要先去空格
# 2.末尾两个7都被去掉了

# 统计字符串中某字符串的出现次数
print(my_str.count('7'))

# 统计字符串的长度
print(len(my_str))