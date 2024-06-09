
def solve(N, G, k, a):
    # Calculate the total cost of building the staircase
    total_cost = 0
    for i in range(N-1):
        total_cost += min((abs(a[i]-a[j])**k for j in range(i+1, N)))
    
    # Return the total cost
    return total_cost

