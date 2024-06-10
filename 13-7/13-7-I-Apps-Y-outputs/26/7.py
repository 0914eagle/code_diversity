
def get_rating(projects, rating):
    for project in projects:
        if rating < project[0]:
            return False
        rating += project[1]
        if rating < 0:
            return False
    return True

def get_possible_order(projects):
    n = len(projects)
    for i in range(n):
        for j in range(i+1, n):
            if projects[i][1] < projects[j][1]:
                projects[i], projects[j] = projects[j], projects[i]
    return projects

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    projects = get_possible_order(projects)
    if get_rating(projects, r):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

