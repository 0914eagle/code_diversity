
def get_order(projects, rating):
    order = []
    for project in projects:
        if rating >= project[0]:
            order.append(project)
            rating += project[1]
    return order

def is_possible(projects, rating):
    order = get_order(projects, rating)
    return all(rating >= project[0] for project in order) and rating >= 0

def main():
    n, r = map(int, input().split())
    projects = []
    for _ in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    print("YES" if is_possible(projects, r) else "NO")

if __name__ == '__main__':
    main()

