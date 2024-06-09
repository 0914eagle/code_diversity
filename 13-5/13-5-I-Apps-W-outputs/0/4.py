
def get_max_sum(n):
    permutation = list(range(1, n+1))
    max_sum = 0
    while True:
        sum_of_remainders = 0
        for i in range(n):
            sum_of_remainders += permutation[i] % (i+1)
        if sum_of_remainders > max_sum:
            max_sum = sum_of_remainders
        if next_permutation(permutation):
            continue
        break
    return max_sum

