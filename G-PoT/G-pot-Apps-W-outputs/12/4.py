
def maximize_hiring_chances(n, k, projects):
    b = [0] * n
    remaining_space = k

    for i in range(n):
        b[i] = min(projects[i], remaining_space)
        remaining_space -= b[i]

    return b

# Input
n, k = map(int, input().split())
projects = list(map(int, input().split()))

# Output
result = maximize_hiring_chances(n, k, projects)
print(*result)
