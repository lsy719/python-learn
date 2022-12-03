# 只执行第一个return

def func():
    return 1, 2, 3

x, y, z = func()
print(x, y, z)