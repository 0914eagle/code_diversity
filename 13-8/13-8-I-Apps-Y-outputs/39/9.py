
def get_rating(projects, rating):
    for project in projects:
        if rating < project[0]:
            return False
        rating += project[1]
        if rating < 0:
            return False
    return True

def get_projects(n):
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    return projects

def main():
    n, r = map(int, input().split())
    projects = get_projects(n)
    if get_rating(projects, r):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

