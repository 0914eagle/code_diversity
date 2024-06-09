
def solve(n, k, arr):
    count = 0
    for i in range(n):
        prod = 1
        sum = 0
        for j in range(i, n):
            prod *= arr[j]
            sum += arr[j]
            if prod // sum == k:
                count += 1
    return count

