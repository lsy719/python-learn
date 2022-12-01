i = 0
while i < 100:
    print(f"Hold my hand *{i}")
    i += 2

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

import random
res = random.randint(1, 100)
get = int(input("猜："))
while get != res:
    if get > res:
        print("大了")
    elif get < res:
        print("小了")
    get = int(input("再猜："))
print(res)

count = 0
res2 = random.randint(1, 50)
flag = True
while flag:
    guess_num = int(input("输入猜的数字："))
    if guess_num == res2:
        print(f"🐂{count}次")
        flag = False
    elif guess_num > res2:
        count += 1
        print("大了")
    else:
        count += 1
        print("小了")

