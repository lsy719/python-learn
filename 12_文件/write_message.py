fileName = 'programming.txt'

# w会清空之前内容
with open(fileName, 'a') as file_obj:
    file_obj.write("I love programming.\n")
    file_obj.write("I love work.\n")