
def find_unused_switches(n, m, cables):
    graph = {i: [] for i in range(1, n + 1)}
    indegree = {i: 0 for i in range(1, n + 1)}
    
    for a, b, _ in cables:
        graph[a].append(b)
        indegree[b] += 1
    
    queue = [1]
    unused_switches = set(range(1, n + 1))
    
    while queue:
        current = queue.pop(0)
        unused_switches.discard(current)
        
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return len(unused_switches), sorted(unused_switches)


if __name__ == '__main__':
    n, m = map(int, input().split())
    cables = [tuple(map(int, input().split())) for _ in range(m)]
    
    k, unused = find_unused_switches(n, m, cables)
    print(k)
    print(*unused)
