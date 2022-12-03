# lambda是关键字

# lambda 传入参数: 函数体（只能一行代码）

def test_func(func):
    res = func(1, 2)
    print(res)

test_func(lambda x, y: x + y)