
def min_operations(a):
    n = len(a)
    count = 0
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
    return count

