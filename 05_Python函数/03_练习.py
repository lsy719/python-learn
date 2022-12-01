# 定义全局变量
money = 5000
name = None

# 要求输入姓名
name = input("what\'s ur name:")
# 定义查询函数
def query(show_header):
    if(show_header):
        print("-------查询余额-------")
    print(f"{name},你有{money}元")


# 定义存款函数
def save(val):
    global money  # money在函数内部定义为全局变量
    money += val
    print(f"-------存款{val}元-------")
    query(False)

# 定义取款函数
def get(val):
    global money  # money在函数内部定义为全局变量
    if money - val >= 0:
        money -= val
        print(f"-------取款{val}元-------")
        query(False)
    else:
        print("爬")

# 定义菜单函数
def menu():
    print("-------主菜单-------")
    print(f"{name},来了啊")
    print("查询余额\t\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("？：")

while True:
    user_select = menu()
    if user_select == "1":
        query(True)
        continue
    elif user_select == "2":
        save(int(input("存多少？：")))
        continue
    elif user_select == "3":
        get(int(input("取多少？：")))
        continue
    else:
        break

