
def get_unfairness(n):
    unfairness = 0
    for i in range(n):
        for j in range(i+1, n):
            unfairness += bin(i^j).count('1')
    return unfairness

