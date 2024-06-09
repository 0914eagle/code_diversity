
def f1(n, m):
    # function to find all possible routes between n towns
    def find_routes(start, end, visited, routes):
        if start == end:
            routes.append(visited[:])
            return
        for i in range(1, n + 1):
            if i not in visited:
                visited.append(i)
                find_routes(start, end, visited, routes)
                visited.pop()
    routes = []
    find_routes(1, 2, [1], routes)
    return len(routes)

def f2(n, m):
    # function to find all possible routes between n towns using at most m roads
    def find_routes(start, end, visited, routes, m):
        if start == end:
            routes.append(visited[:])
            return
        for i in range(1, n + 1):
            if i not in visited and m > 0:
                visited.append(i)
                find_routes(start, end, visited, routes, m - 1)
                visited.pop()
    routes = []
    find_routes(1, 2, [1], routes, m)
    return len(routes)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f2(n, m))

