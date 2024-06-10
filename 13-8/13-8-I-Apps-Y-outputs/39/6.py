
def get_order(projects, r):
    order = []
    for project in projects:
        if r >= project[0]:
            order.append(project)
            r += project[1]
        else:
            return None
    return order

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    order = get_order(projects, r)
    if order:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

