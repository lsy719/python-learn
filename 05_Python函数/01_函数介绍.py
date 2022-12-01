str1 = 'qvo'
str2 = 'revolution'
str3 = 'standby'

# 内置函数
print(len(str1), len(str2), len(str3))


# 自定义函数
def lsy_len(data):
    count = 0
    for i in data:
        count += 1
    return count


print(lsy_len(str1), lsy_len(str2), lsy_len(str3))


def doit():
    print("爬")


print(doit(), type(doit()), doit, type(doit))


# 函数没有return 返回None, NoneType


# 函数说明文档
def quarantine(bt):
    """
    :param bt:
    :return:
    """
    if bt > 37.3:
        print("带走")
    else:
        print("爬")


quarantine(38)

quarantine(36)
