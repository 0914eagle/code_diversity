
def get_max_sum(n):
    permutation = list(range(1, n+1))
    max_sum = 0
    while True:
        remainder_sum = 0
        for i in range(n):
            remainder = i % permutation[i]
            remainder_sum += remainder
        if remainder_sum > max_sum:
            max_sum = remainder_sum
        if next_permutation(permutation):
            continue
        break
    return max_sum

