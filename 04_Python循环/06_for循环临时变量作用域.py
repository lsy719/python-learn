for i in range(5):
    print(i)
print(i)

i = 100 # i在下面又被重新赋值了
for i in range(3):
    print(i)
print(i)
# 规范问题
# 临时变量，在编程规范上，作用范围（域），只限定在for循环内部

# 如果for循环外部访问临时变量
# ·实际是可以访问到的
# ·在变成规范上，是不允许的、 不建议这么做

# 这种限定
# · 是变成规范的限定，而非强制限定
# · 不遵守也没事，但不建议
# · 如需要访问临时变量，可以与现在循环外定义它