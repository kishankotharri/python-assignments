num = int(input("Enter number: "))
total = 1

for x in range(num,0,-1):
    print(x)
    total *= x

print("factorial of a number:", total)