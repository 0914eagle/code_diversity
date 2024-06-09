
def solve(A, B, C, X, Y):
    # Calculate the cost of buying X A-pizzas and Y B-pizzas separately
    cost_A = X * A
    cost_B = Y * B
    
    # Calculate the cost of buying two AB-pizzas and rearranging them into one A-pizza and one B-pizza
    cost_AB = 2 * C
    
    # Calculate the total cost of buying X A-pizzas and Y B-pizzas
    total_cost = cost_A + cost_B
    
    # If the total cost is greater than or equal to the cost of buying two AB-pizzas and rearranging them, then it is optimal to buy two AB-pizzas and rearrange them
    if total_cost >= cost_AB:
        return cost_AB
    
    # Otherwise, return the total cost of buying X A-pizzas and Y B-pizzas
    else:
        return total_cost

