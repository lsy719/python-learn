import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("输入你的名称")
    with open(filename, 'w') as f:
        json.dump(username, f)
else:
    print(f'greeing, {username}')
