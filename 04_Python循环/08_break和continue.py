# 需要
# 暂时跳过某次循环，直接进行下一次
# 提前推出循环，不再继续

# 某公司，账户有1w元，给20名员工发工资。
# · 员工编号从1到20，从编号1开始，依次领取工资，没人可领取1000元
# · 领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
# · 如果工资发完了，结束发工资
import random
balance = 10000
for u in range(1,21):
    if balance <= 0:
        print("发完了，都爬")
        break
    p = random.randint(1,10)
    if p < 5:
        print(f"员工{u},绩效分{p},爬，下一位")
    else:
        if balance >= 1000:
            balance -= 1000
            print(f"员工{u},绩效分{p},发1000,剩余{balance}")



