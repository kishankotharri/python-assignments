l1 = [1, 2, 3, 4, 5] 
l2 = [4, 5, 6, 7, 8]

arr = []

for n in l1:
    if n in l2:
        arr.append(n)

print(arr)