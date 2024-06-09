
def maximize_value(n, k, a):
    b = [0] * n
    remaining_space = k

    for i in range(n):
        if remaining_space == 0:
            break
        max_projects = min(remaining_space, a[i])
        b[i] = max_projects
        remaining_space -= max_projects

    return b

# Input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output
result = maximize_value(n, k, a)
print(*result)
