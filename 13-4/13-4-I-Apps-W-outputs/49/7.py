
def solve(n, m, arr):
    result = 1
    for i in range(n):
        for j in range(i+1, n):
            result = (result * abs(arr[i] - arr[j])) % m
    return result

