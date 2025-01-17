string = "Hello, World!"

str_list = list(string)

count = 0

for x in str_list:
    if x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        count += 1

print("Number of vowels:", count)