
def solve():
    H, N = map(int, input().split())
    spells = []
    for i in range(N):
        A, B = map(int, input().split())
        spells.append((A, B))
    
    # Sort the spells in descending order of their cost
    spells.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the minimum total Magic Points to 0
    min_points = 0
    
    # Loop through the spells and cast the most expensive spell that can decrease the monster's health
    for A, B in spells:
        if H - A >= 0:
            min_points += B
            H -= A
    
    return min_points

