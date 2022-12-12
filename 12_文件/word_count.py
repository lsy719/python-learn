def count_words(filename):
    """计算一个文件的单词数量"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print('idiot')
        pass # 保持静默
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has about {num_words} words.')

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)