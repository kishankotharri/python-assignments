r = open("demo.txt", "r")

count = 0

for line in r:    
    count += 1

print("Total Line: ", count)