
def count_apples(n, p):
    apples = 1
    for i in range(n-1):
        apples += 1 - (apples-1) % p[i]
    return apples

