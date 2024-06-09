
def solve(m, k, a, b):
    # Calculate the sum of the target fractions
    sum_f = sum(a)

    # Calculate the current number of sweets eaten for each type
    s = [0] * m
    for i in range(k):
        s[b[i] - 1] += 1

    # Calculate the maximum number of additional sweets that can be bought
    max_sweets = 0
    for i in range(m):
        if s[i] == 0:
            max_sweets += 1
        elif s[i] == sum_f - 1:
            max_sweets += 2
        else:
            max_sweets += 1

    return max_sweets

