
def solve(n, d, a, m):
    # Calculate the total cost of using all the hooks
    total_cost = sum(a)
    
    # Calculate the fine for each guest
    fine = d * m
    
    # Return the difference between the total cost and the fine
    return total_cost - fine

