filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print('idiot')
else:
    # 计算单词数
    words = contents.split()
    num_words = len(words)
    print(num_words)
