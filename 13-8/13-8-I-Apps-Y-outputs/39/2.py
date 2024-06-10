
def get_order(n, r, projects):
    order = []
    for i in range(n):
        project = projects[i]
        if r >= project[0]:
            order.append(i)
            r += project[1]
    return "YES" if len(order) == n else "NO"

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    print(get_order(n, r, projects))

if __name__ == '__main__':
    main()

