# 位置参数 - 默认使用形式

def user_info(name, age, gender):
    print(name, age, gender)


# 关键字参数 不按照参数定义顺序传参
user_info(age=22, name='lsy', gender='男')


# 缺省参数(默认值), 默认值必须是最后一个参数设置
def user_info2(name, age, gender='男'):
    print(name, age, gender)


user_info2('lsy', 22)

# 不定长 - 位置不定长， *号
# 也叫可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以)的场景
# 作用：当调用函数时不确定参数个数时，可以使用不定长参数
def user_info3(*args):
    print(args)

# 合并到args中的参数为一个元组
user_info3()
user_info3(1, 2, 3)

# 不定长 - 关键字不定长 **号
def user_info4(**kwargs):
    print(kwargs)
# 传递时按关键字去传,组成一个字典
user_info4(name = "lsy", age = 22)

