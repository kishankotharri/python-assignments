Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

New_list = {}

for x in Input_list:
    if x in New_list.keys():
        New_list[x] += 1
    else:
        New_list[x] = 1

print("Frequency count:", New_list)