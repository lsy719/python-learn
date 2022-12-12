def get_formatted_name(first, last, middle ='',):
    if middle:
        full_name = f"{first} {middle} {last}"
    # print(full_name)
    # 似乎会把一句话中每个单词首字母都大写，但是这是作为一个字符串啊？
    else:
        full_name = f'{first} {last}'
    return full_name.title()
