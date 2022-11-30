# 方式1： 使用print直接输出类型信息
print(type("lsy"))
print(type(666))
print(type(3.14159))

# 方式2： 使用变量存储type()语句的结果
string_type = type("lsy")
int_type = type(111)
float_type = type(11.11)
print(string_type, int_type, float_type)

# 方式3： 使用type()语句，查看变量中存储的数据类型信息
str = "lsy"
print(type(str))