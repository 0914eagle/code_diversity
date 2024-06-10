
def get_rating_after_projects(projects, rating):
    rating_after_projects = []
    for project in projects:
        rating_after_projects.append(rating + project[1])
    return rating_after_projects

def is_possible(projects, rating):
    rating_after_projects = get_rating_after_projects(projects, rating)
    for i in range(len(projects)):
        if rating_after_projects[i] < 0:
            return False
    return True

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    if is_possible(projects, r):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

