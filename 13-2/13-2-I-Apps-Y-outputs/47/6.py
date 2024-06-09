
def solve(A, B, C, X, Y):
    # Calculate the cost of buying X A-pizzas and Y B-pizzas separately
    cost_A = X * A
    cost_B = Y * B
    
    # Calculate the cost of buying two AB-pizzas and rearranging them into A-pizzas and B-pizzas
    cost_AB = 2 * C
    cost_A_from_AB = cost_AB // 2
    cost_B_from_AB = cost_AB // 2
    
    # Calculate the total cost of buying X A-pizzas and Y B-pizzas
    total_cost = cost_A + cost_B
    
    # If buying two AB-pizzas and rearranging them is cheaper than buying X A-pizzas and Y B-pizzas separately, return the total cost of buying two AB-pizzas and rearranging them
    if cost_AB < total_cost:
        return cost_AB
    # Otherwise, return the total cost of buying X A-pizzas and Y B-pizzas separately
    else:
        return total_cost

