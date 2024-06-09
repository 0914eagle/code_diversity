
def get_min_cost(A, B, C, X, Y):
    # Calculate the cost of buying A-pizzas and B-pizzas separately
    cost_A = A * X
    cost_B = B * Y
    
    # Calculate the cost of buying AB-pizzas and rearranging them into A-pizzas and B-pizzas
    cost_AB = C * (X // 2 + Y // 2)
    
    # Return the minimum of the two costs
    return min(cost_A + cost_B, cost_AB)

def main():
    A, B, C, X, Y = map(int, input().split())
    print(get_min_cost(A, B, C, X, Y))

if __name__ == '__main__':
    main()

