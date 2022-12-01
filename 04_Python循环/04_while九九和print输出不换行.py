print("Hello", end="")
print("World", end="")
print("\n")
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i}*{j}={i*j}\t", end="")
        j += 1;
    print() # print空内容，就是输出一个换行
    i += 1

