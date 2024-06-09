
def solve():
    H, N = map(int, input().split())
    spells = []
    for i in range(N):
        A, B = map(int, input().split())
        spells.append((A, B))
    
    # Sort the spells in descending order of their cost
    spells.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the total cost to 0
    total_cost = 0
    
    # Loop through the spells and cast the most expensive one that can still decrease the monster's health
    while H > 0:
        for A, B in spells:
            if H - A >= 0:
                H -= A
                total_cost += B
                break
    
    return total_cost

