number_list = [7, 2, 5, 1, 9, 3]

number_list.sort()

print(number_list)

n = len(number_list)

if n % 2 == 0:
    median = (number_list[n // 2 - 1] + number_list[n // 2]) / 2
else:
    median = number_list[n // 2]

print("Median", median)