
def maximize_hiring_chances(n, k, projects):
    total_projects = sum(projects)
    b = [min(projects[i], k // n) for i in range(n)]
    remaining_projects = k - sum(b)
    
    while remaining_projects > 0:
        max_idx = b.index(max(b))
        b[max_idx] += 1
        remaining_projects -= 1
    
    return b

# Input
n, k = map(int, input().split())
projects = list(map(int, input().split()))

# Output
result = maximize_hiring_chances(n, k, projects)
print(*result)
