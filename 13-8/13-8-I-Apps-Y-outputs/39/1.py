
def get_projects(n):
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    return projects

def is_possible(projects, r):
    for a, b in projects:
        if r < a:
            return False
        r += b
        if r < 0:
            return False
    return True

def solve(projects, r):
    if is_possible(projects, r):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    n, r = map(int, input().split())
    projects = get_projects(n)
    print(solve(projects, r))

