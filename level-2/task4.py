arr = [1, 2, 3, 4, 5]
D = 4
total = len(arr)
new_arr = []

for n in range(0,total):

    if D > total-1:
        D=0
    
    new_arr.append(arr[D])

    D += 1

print(new_arr)