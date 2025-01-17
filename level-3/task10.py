def count_customers_left(N, S):
    occupied = set()
    visited = {}
    walked_away = 0

    for customer in S:
        
        if customer not in visited:            
            visited[customer] = 'Yes'
            if len(occupied) < N:
                occupied.add(customer)
            else:
                walked_away += 1
        else:
            if customer in occupied:
                occupied.remove(customer)

    return walked_away

N1 = 3
S1 = "GACCBDDBAGEE"
print("Output for Example 1:", count_customers_left(N1, S1))

N2 = 1
S2 = "ABCBAC"
print("Output for Example 2:", count_customers_left(N2, S2))
