
def f1(n, c, encounters):
    # create a graph with n nodes and c edges
    graph = [[] for _ in range(n + 1)]
    for a, b, y in encounters:
        graph[a].append((b, y))
        graph[b].append((a, y))
    
    # find the earliest year when all nodes are connected
    years = [float('inf') for _ in range(n + 1)]
    queue = [1]
    years[1] = 0
    while queue:
        node = queue.pop(0)
        for neighbor, year in graph[node]:
            if year < years[neighbor]:
                years[neighbor] = year
                queue.append(neighbor)
    
    # find the maximum year when all nodes are connected
    max_year = 0
    for node in range(1, n + 1):
        if years[node] > max_year:
            max_year = years[node]
    
    # check if it is possible to divide the participants into two parts
    # such that no part contains more than 2/3 of the participants
    # and all people in the first part first met before year Y
    # and all people in the second part first met in or after year Y
    for node in range(1, n + 1):
        if years[node] < max_year:
            return max_year
    return 'Impossible'

def f2(n, c, encounters):
    # create a graph with n nodes and c edges
    graph = [[] for _ in range(n + 1)]
    for a, b, y in encounters:
        graph[a].append((b, y))
        graph[b].append((a, y))
    
    # find the earliest year when all nodes are connected
    years = [float('inf') for _ in range(n + 1)]
    queue = [1]
    years[1] = 0
    while queue:
        node = queue.pop(0)
        for neighbor, year in graph[node]:
            if year < years[neighbor]:
                years[neighbor] = year
                queue.append(neighbor)
    
    # find the maximum year when all nodes are connected
    max_year = 0
    for node in range(1, n + 1):
        if years[node] > max_year:
            max_year = years[node]
    
    # check if it is possible to divide the participants into two parts
    # such that no part contains more than 2/3 of the participants
    # and all people in the first part first met before year Y
    # and all people in the second part first met in or after year Y
    for node in range(1, n + 1):
        if years[node] < max_year:
            return max_year
    return 'Impossible'

if __name__ == '__main__':
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(f1(n, c, encounters))
    print(f2(n, c, encounters))

