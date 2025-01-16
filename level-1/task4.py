start = int(input("Enter start number: "))
stop = int(input("Enter stop number: "))

sum_odd = 0

for x in range(start,stop):
    if x % 2 != 0:
        sum_odd += x

print("Sum of odd numbers:", sum_odd)