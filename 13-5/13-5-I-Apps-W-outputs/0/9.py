
def get_max_sum(n):
    permutation = list(range(1, n+1))
    max_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum = (permutation[i] % permutation[j]) + (permutation[j] % permutation[i])
            if sum > max_sum:
                max_sum = sum
    return max_sum

