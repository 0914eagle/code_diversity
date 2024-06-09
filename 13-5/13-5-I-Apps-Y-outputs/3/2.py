
def get_minimum_cost(A, B, C, X, Y):
    # Calculate the cost of buying X A-pizzas and Y B-pizzas separately
    cost_A = X * A
    cost_B = Y * B
    
    # Calculate the cost of buying two AB-pizzas and rearranging them into A-pizzas and B-pizzas
    cost_AB = 2 * C
    cost_A_from_AB = A
    cost_B_from_AB = B
    
    # Calculate the total cost of buying X A-pizzas and Y B-pizzas
    total_cost = cost_A + cost_B
    
    # Calculate the total cost of buying two AB-pizzas and rearranging them into A-pizzas and B-pizzas
    total_cost_AB = cost_AB + cost_A_from_AB + cost_B_from_AB
    
    # Return the minimum of the two costs
    return min(total_cost, total_cost_AB)

def main():
    A, B, C, X, Y = map(int, input().split())
    print(get_minimum_cost(A, B, C, X, Y))

if __name__ == '__main__':
    main()

