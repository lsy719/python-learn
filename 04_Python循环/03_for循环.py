name = "chinaunicom"

for i in name:
    print(f"{i} ", end="")
print()
# for 临时变量 in 待处理的数据集（序列）
# 无法定义循环条件，只能被动取出数据处理
# 空格缩进

name2 = 'I had wandered the walls forever, but came upon a way for my return.'
count = 0
for i in name2:
    if i == 't':
        count += 1
print(f"\"{name2}\"中\'t\'的数量：{count}")