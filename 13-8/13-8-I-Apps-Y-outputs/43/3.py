
def largest_perfect_power(x):
    for i in range(x, 0, -1):
        if i ** 0.5 == int(i ** 0.5):
            return i
    return 1

