
def solve(A, B, C, X, Y):
    # Calculate the cost of buying X A-pizzas and Y B-pizzas separately
    cost_A = X * A
    cost_B = Y * B
    
    # Calculate the cost of buying two AB-pizzas and rearranging them into one A-pizza and one B-pizza
    cost_AB = 2 * C
    
    # Calculate the total cost of buying X A-pizzas and Y B-pizzas
    total_cost = cost_A + cost_B
    
    # If the cost of buying two AB-pizzas and rearranging them is less than the total cost, return the cost of buying two AB-pizzas and rearranging them
    if cost_AB < total_cost:
        return cost_AB
    # Otherwise, return the total cost
    else:
        return total_cost

