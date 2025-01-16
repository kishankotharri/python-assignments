num = int(input("Enter number: "))
sum = 0
is_perfect = False

for x in range(0,num):
    if(num == sum):
        is_perfect = True
        break
    sum += x

if is_perfect == True:
    print("Yes, perfect number")
else:
    print("No, perfect number")