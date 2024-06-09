
def get_permutation(n, k):
    permutation = []
    for i in range(1, n+1):
        permutation.append(i)
    for i in range(n):
        if k > 0:
            permutation[2*i-1], permutation[2*i] = permutation[2*i], permutation[2*i-1]
            k -= 1
    return permutation

