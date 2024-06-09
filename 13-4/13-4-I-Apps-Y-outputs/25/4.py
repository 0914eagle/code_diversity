
def get_dog_attack(A, B, C, D, P, M, G):
    # Calculate the number of minutes until the next aggressive period for each dog
    aggressive_period_1 = (P - 1) % (A + B)
    aggressive_period_2 = (M - 1) % (C + D)
    aggressive_period_3 = (G - 1) % (C + D)

    # Check if any of the dogs are aggressive during the postman's visit
    if aggressive_period_1 == 0 or aggressive_period_1 == A:
        return "both"
    elif aggressive_period_2 == 0 or aggressive_period_2 == C:
        return "both"
    elif aggressive_period_3 == 0 or aggressive_period_3 == C:
        return "both"
    else:
        return "none"

def get_dog_attack_2(A, B, C, D, P, M, G):
    # Calculate the number of minutes until the next aggressive period for each dog
    aggressive_period_1 = (P - 1) % (A + B)
    aggressive_period_2 = (M - 1) % (C + D)
    aggressive_period_3 = (G - 1) % (C + D)

    # Check if any of the dogs are aggressive during the milkman's visit
    if aggressive_period_1 == 0 or aggressive_period_1 == A:
        return "one"
    elif aggressive_period_2 == 0 or aggressive_period_2 == C:
        return "one"
    elif aggressive_period_3 == 0 or aggressive_period_3 == C:
        return "one"
    else:
        return "none"

def get_dog_attack_3(A, B, C, D, P, M, G):
    # Calculate the number of minutes until the next aggressive period for each dog
    aggressive_period_1 = (P - 1) % (A + B)
    aggressive_period_2 = (M - 1) % (C + D)
    aggressive_period_3 = (G - 1) % (C + D)

    # Check if any of the dogs are aggressive during the garbage man's visit
    if aggressive_period_1 == 0 or aggressive_period_1 == A:
        return "none"
    elif aggressive_period_2 == 0 or aggressive_period_2 == C:
        return "none"
    elif aggressive_period_3 == 0 or aggressive_period_3 == C:
        return "none"
    else:
        return "both"

if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    P, M, G = map(int, input().split())
    print(get_dog_attack(A, B, C, D, P, M, G))
    print(get_dog_attack_2(A, B, C, D, P, M, G))
    print(get_dog_attack_3(A, B, C, D, P, M, G))

