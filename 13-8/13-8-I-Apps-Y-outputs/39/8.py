
def get_possible_order(projects, rating):
    
    order = []
    for project in projects:
        if rating >= project[0]:
            order.append(project)
            rating += project[1]
    return order

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    order = get_possible_order(projects, r)
    if len(order) == n:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

