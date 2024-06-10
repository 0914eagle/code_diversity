
def get_rating(rating, projects, i):
    return max(rating + projects[i][1], 0)

def can_complete_projects(rating, projects):
    for i in range(len(projects)):
        if rating < projects[i][0]:
            return False
        rating = get_rating(rating, projects, i)
    return True

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    if can_complete_projects(r, projects):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

