num = int(input("Enter number: "))

while num >= 10:
    num = sum(int(digit) for digit in str(num))
    
print(num)