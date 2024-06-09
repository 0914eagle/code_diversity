
def f1(A, B, C, D, P, M, G):
    # Calculate the number of minutes until the next aggressive period
    aggressive_period_1 = (P - 1) % (A + B)
    aggressive_period_2 = (M - 1) % (C + D)
    aggressive_period_3 = (G - 1) % (C + D)

    # Check if the postman is attacked
    if aggressive_period_1 == 0 or aggressive_period_1 == A:
        return "one"
    elif aggressive_period_2 == 0 or aggressive_period_2 == C:
        return "one"
    elif aggressive_period_3 == 0 or aggressive_period_3 == C:
        return "one"
    else:
        return "none"

def f2(A, B, C, D, P, M, G):
    # Calculate the number of minutes until the next aggressive period
    aggressive_period_1 = (P - 1) % (A + B)
    aggressive_period_2 = (M - 1) % (C + D)
    aggressive_period_3 = (G - 1) % (C + D)

    # Check if the milkman is attacked
    if aggressive_period_1 == 0 or aggressive_period_1 == A:
        return "one"
    elif aggressive_period_2 == 0 or aggressive_period_2 == C:
        return "one"
    elif aggressive_period_3 == 0 or aggressive_period_3 == C:
        return "one"
    else:
        return "none"

def f3(A, B, C, D, P, M, G):
    # Calculate the number of minutes until the next aggressive period
    aggressive_period_1 = (P - 1) % (A + B)
    aggressive_period_2 = (M - 1) % (C + D)
    aggressive_period_3 = (G - 1) % (C + D)

    # Check if the garbage man is attacked
    if aggressive_period_1 == 0 or aggressive_period_1 == A:
        return "one"
    elif aggressive_period_2 == 0 or aggressive_period_2 == C:
        return "one"
    elif aggressive_period_3 == 0 or aggressive_period_3 == C:
        return "one"
    else:
        return "none"

if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    P, M, G = map(int, input().split())
    print(f1(A, B, C, D, P, M, G))
    print(f2(A, B, C, D, P, M, G))
    print(f3(A, B, C, D, P, M, G))

