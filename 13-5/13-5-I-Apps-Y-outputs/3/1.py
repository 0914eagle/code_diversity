
def f1(A, B, C, X, Y):
    # Calculate the cost of buying X A-pizzas and Y B-pizzas separately
    cost_A = A * X
    cost_B = B * Y

    # Calculate the cost of buying two AB-pizzas and rearranging them into one A-pizza and one B-pizza
    cost_AB = 2 * C
    cost_A_rearrange = A
    cost_B_rearrange = B

    # Return the minimum cost
    return min(cost_A + cost_B, cost_AB + cost_A_rearrange + cost_B_rearrange)

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    A, B, C, X, Y = map(int, input().split())
    print(f1(A, B, C, X, Y))

