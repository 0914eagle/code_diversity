
def solve(N, G, k, a):
    # Calculate the total cost of building the staircase
    total_cost = 0
    for i in range(N-1):
        total_cost += min([(a[i+1]-a[i])**k for v in range(a[i], a[i+1]+1)])
    
    # Return the total cost
    return total_cost

