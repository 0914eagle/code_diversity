
def get_projects_order(projects, rating):
    order = []
    for project in projects:
        if rating >= project[0]:
            order.append(project)
            rating += project[1]
    return order

def is_possible(projects, rating):
    order = get_projects_order(projects, rating)
    return len(order) == len(projects)

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    print("YES") if is_possible(projects, r) else print("NO")

if __name__ == '__main__':
    main()

