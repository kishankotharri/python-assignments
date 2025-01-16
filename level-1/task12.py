num = int(input("Enter number: "))
num = str(num)

num_lists = list(num)
reversed_lists = num_lists[::-1]

new_num = ''.join(reversed_lists)
new_num = int(new_num)

print(new_num)