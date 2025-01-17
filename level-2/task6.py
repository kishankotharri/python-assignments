n = 5

is_recursion = True

while is_recursion:

    if n <= 0:
        is_recursion = False
        break

    if n == 1:
        is_recursion = True
        break
		
    a = n % 2
    if a == 0:
        n = n // 2
        is_recursion = True
    else:
        is_recursion = False
        break

print(is_recursion)