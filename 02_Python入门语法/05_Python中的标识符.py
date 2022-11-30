# 规则1：内容限定，限定只能使用：中文、英文、数字、下划线，注意：不能以数字开头
# 1_name = "lsy"
# name_! = "lsy"
name_ = "lsy"
_name = "lsy"
name_1 = "lsy"

# 规则2：大小写敏感
name = "lsy"
Name = "lsy"
print(name, Name)

# 规则3：不可使用关键字
# def = 1