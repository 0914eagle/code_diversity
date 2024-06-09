
def get_max_sum(n):
    permutation = list(range(1, n+1))
    max_sum = 0
    while True:
        current_sum = 0
        for i in range(n):
            current_sum += permutation[i] % (i+1)
        if current_sum > max_sum:
            max_sum = current_sum
        if next_permutation(permutation):
            continue
        break
    return max_sum

