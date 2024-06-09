
def maximize_value(n, k, projects):
    total_projects = sum(projects)
    b = [0] * n
    remaining_projects = k
    for i in range(n):
        b[i] = min(projects[i], remaining_projects)
        remaining_projects -= b[i]
    return b

n, k = map(int, input().split())
projects = list(map(int, input().split()))

result = maximize_value(n, k, projects)
print(*result)
