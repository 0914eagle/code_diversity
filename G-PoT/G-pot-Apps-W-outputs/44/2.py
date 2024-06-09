
def count_sets(n, m):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            candies = i**2 + j**2
            if candies % m == 0:
                count += 1
    return count

n, m = map(int, input().split())
result = count_sets(n, m)
print(result)
