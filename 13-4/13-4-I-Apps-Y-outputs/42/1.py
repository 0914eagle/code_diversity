
def find_subordinates(n, a):
    subordinates = [0] * (n + 1)
    for i in range(2, n + 1):
        subordinates[a[i - 1]] += 1
    return subordinates

