
def solve():
    H, N = map(int, input().split())
    spells = []
    for i in range(N):
        A, B = map(int, input().split())
        spells.append((A, B))
    
    # Sort the spells in descending order of their cost
    spells.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the total cost as 0
    total_cost = 0
    
    # Loop through the spells and cast them until the monster's health becomes 0 or below
    for A, B in spells:
        total_cost += B
        H -= A
        if H <= 0:
            break
    
    return total_cost

