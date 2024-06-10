
def get_rating_after_completing_projects(rating, projects):
    rating_after_completing_projects = rating
    for project in projects:
        rating_after_completing_projects += project[1]
        if rating_after_completing_projects < 0:
            return False
    return True

def get_possible_order_of_projects(n, r, projects):
    possible_orders = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if get_rating_after_completing_projects(r, [(projects[i], projects[j], projects[k])]):
                    possible_orders.append((i, j, k))
    return possible_orders

def main():
    n, r = map(int, input().split())
    projects = []
    for i in range(n):
        a, b = map(int, input().split())
        projects.append((a, b))
    possible_orders = get_possible_order_of_projects(n, r, projects)
    if possible_orders:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

