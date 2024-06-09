
def f1(A, B, C, X, Y):
    # Calculate the cost of buying X A-pizzas and Y B-pizzas directly
    cost_direct = A * X + B * Y
    
    # Calculate the cost of buying two AB-pizzas and rearranging them into one A-pizza and one B-pizza
    cost_rearrange = 2 * C + min(X, Y)
    
    # Return the minimum cost
    return min(cost_direct, cost_rearrange)

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    A, B, C, X, Y = map(int, input().split())
    print(f1(A, B, C, X, Y))

