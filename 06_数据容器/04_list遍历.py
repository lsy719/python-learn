# while循环遍历
def list_while_func():
    my_list = ['html', 'css', 'js']
    i = 0
    while i < len(my_list):
        print(my_list[i])
        i += 1

list_while_func()

def list_for_func():
    my_list = ['html', 'css', 'js']
    for elem in my_list:
        print(elem)

def list_for_func2():
    my_list = ['html', 'css', 'js']
    for i in range(0, len(my_list)):
        print(my_list[i])

list_for_func()
list_for_func2()