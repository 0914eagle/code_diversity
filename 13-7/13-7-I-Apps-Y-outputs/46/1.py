
def largest_perfect_power(x):
    # Find the largest perfect power that is at most x
    for i in range(x, 1, -1):
        if i ** 0.5 == int(i ** 0.5):
            return i
    return 1

