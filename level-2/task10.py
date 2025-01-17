n = int(input("Enter the number of piles (n): "))

if n <= 0:
    print("The number of piles must be a positive integer.")
  
else:
    piles = []

    if n % 2 == 0:
        for x in range(2, n, 2):
            piles.append(x)
    else:
        for x in range(1, n, 2):
            piles.append(x)
    
    print("Number of stones in each pile:", piles)

    piles2 = [n]
    for x in range(1, n):
        piles2.append(piles2[-1] + 2)
    
    print("Number of stones in each pile2:", piles2)