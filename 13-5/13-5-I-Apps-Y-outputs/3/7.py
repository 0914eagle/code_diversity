
def f1(A, B, C, X, Y):
    # Calculate the cost of buying X A-pizzas and Y B-pizzas directly
    cost_direct = X * A + Y * B
    
    # Calculate the cost of buying two AB-pizzas and rearranging them into A-pizzas and B-pizzas
    cost_rearrange = 2 * C
    
    # Return the minimum of the two costs
    return min(cost_direct, cost_rearrange)

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    A, B, C, X, Y = map(int, input().split())
    print(f1(A, B, C, X, Y))

