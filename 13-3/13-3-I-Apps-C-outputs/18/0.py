
def f1(W, S, C, K):
    # Initialize variables
    wolf_count = W
    sheep_count = S
    cabbage_count = C
    boat_capacity = K
    safe_combinations = 0

    # Iterate through all possible combinations of items on the bank
    for w in range(0, wolf_count + 1):
        for s in range(0, sheep_count + 1):
            for c in range(0, cabbage_count + 1):
                # Check if the combination is safe
                if wolf_eats_sheep(w, s) and sheep_eats_cabbage(s, c):
                    safe_combinations += 1

    # Check if the safe combinations are greater than or equal to the total number of items
    if safe_combinations >= (wolf_count + sheep_count + cabbage_count):
        return "YES"
    else:
        return "NO"

def f2(W, S, C, K):
    # Initialize variables
    wolf_count = W
    sheep_count = S
    cabbage_count = C
    boat_capacity = K
    safe_combinations = 0

    # Iterate through all possible combinations of items on the bank
    for w in range(0, wolf_count + 1):
        for s in range(0, sheep_count + 1):
            for c in range(0, cabbage_count + 1):
                # Check if the combination is safe
                if wolf_eats_sheep(w, s) and sheep_eats_cabbage(s, c):
                    safe_combinations += 1

    # Check if the safe combinations are greater than or equal to the total number of items
    if safe_combinations >= (wolf_count + sheep_count + cabbage_count):
        return "YES"
    else:
        return "NO"

def wolf_eats_sheep(w, s):
    return w >= s

def sheep_eats_cabbage(s, c):
    return s >= c

if __name__ == '__main__':
    W, S, C, K = map(int, input().split())
    print(f1(W, S, C, K))
    print(f2(W, S, C, K))

