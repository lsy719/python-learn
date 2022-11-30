salary = 1800
salary -= 1
if salary == 1800:
    print("笑哈哈")
else:
    print("呜呜呜")

salary = int(input("输入工资："))
if salary < 1800:
    print("笑哈哈")
    if salary < 100:
        print("爬")
elif salary < 10000:
    print("呜呜呜")
else:
    print("死了")

import random
num = random.randint(1, 10)
input1 = int(input("猜:"))
if input1 == num:
    print('第一次猜对了')
else:
    print('第一次猜错了')
    if input1 < num:
        print("小了")
    else:
        print("大了")
    input2 = int(input("猜第二次:"))
    if input2 == num:
        print("第二猜对了")
    else:
        print("第二次猜错了")
        if input2 < num:
            print("小了")
        else:
            print("大了")
        input3 = int(input("猜第三次:"))
        if input3 == num:
            print("第三次猜对了")
        else:
            print(f"傻逼,是{num}")