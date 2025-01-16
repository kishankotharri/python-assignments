list1 = [1, 2, 2, 3, 4, 4, 5, 5]

arr = []

for n in list1:
    if n not in arr:
        arr.append(n)

print(arr)