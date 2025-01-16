text = input("Enter string and number: ")
alph = 0
num = 0

for x in text:
    if x.isdigit():
        num += 1
    else:
        alph += 1

print("Alphabets:", alph, "& Number:", num)