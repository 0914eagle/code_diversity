
def is_connected(graph, start, end):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def find_roads(graph, gangs):
    roads = []
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if gangs[i] != gangs[j] and is_connected(graph, i, j):
                roads.append((i, j))
    return roads

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        gangs = list(map(int, input().split()))
        graph = [[] for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                if gangs[i] != gangs[j]:
                    graph[i].append(j)
                    graph[j].append(i)
        roads = find_roads(graph, gangs)
        if len(roads) == n-1:
            print("YES")
            for road in roads:
                print(*road)
        else:
            print("NO")

if __name__ == '__main__':
    main()

