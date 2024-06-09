
def get_min_cost(A, B, C, X, Y):
    # Calculate the cost of buying X A-pizzas and Y B-pizzas directly
    direct_cost = A * X + B * Y

    # Calculate the cost of buying two AB-pizzas and rearranging them into one A-pizza and one B-pizza
    ab_cost = 2 * C
    a_cost = A
    b_cost = B
    rearranged_cost = ab_cost + min(a_cost, b_cost)

    # Return the minimum of the two costs
    return min(direct_cost, rearranged_cost)

def main():
    A, B, C, X, Y = map(int, input().split())
    print(get_min_cost(A, B, C, X, Y))

if __name__ == '__main__':
    main()

