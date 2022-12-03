def test_func(func):
    res = func(1, 2)
    return res

def compute(x, y):
    return x + y

res = test_func(compute)
print(res)