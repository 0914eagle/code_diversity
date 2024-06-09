
n, k = map(int, input().split())
a = list(map(int, input().split()))

b = [0] * n
remaining_projects = k

for i in range(n):
    b[i] = min(a[i], remaining_projects)
    remaining_projects -= b[i]

print(*b)
