with open('./pi_digits.txt') as file_object:
    # contents = file_object.read()
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()
# print(contents)
pi_string = ''
for line in lines:
    print(line.rstrip())
    pi_string += line.strip()

print(pi_string)

# 逐行读取
with open('./pi_million_digits.txt') as big_file:
    lines = big_file.readlines()

big_pi_string = ''
for line in lines:
    # print(line.strip())
    big_pi_string += line.strip()
print(big_pi_string)
birthday = '1108'
if birthday in big_pi_string:
    print("There is")
else:
    print("nothing")
