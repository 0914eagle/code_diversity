
def get_projects(n):
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    return projects

def get_rating(projects, r):
    rating = r
    for project in projects:
        if rating < project[0]:
            return False
        rating += project[1]
    return True

def solve(n, r, projects):
    if get_rating(projects, r):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    n, r = map(int, input().split())
    projects = get_projects(n)
    print(solve(n, r, projects))

