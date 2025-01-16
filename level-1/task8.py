num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

larger = max(num1, num2)

while True:
    if larger % num1 == 0 and larger % num2 == 0:
        break
    larger += 1
    
print("LCM is",larger)