
import collections

def get_graph(n, m):
    graph = collections.defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph

def get_pigs(n, p):
    return set(map(int, input().split()))

def bfs(graph, start):
    visited = set()
    queue = collections.deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    return visited

def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return visited

def min_wolves(graph, pigs):
    visited = set()
    for pig in pigs:
        visited |= bfs(graph, pig)
    return len(pigs) - len(visited)

def main():
    v, p = map(int, input().split())
    graph = get_graph(v, v-1)
    pigs = get_pigs(v, p)
    print(min_wolves(graph, pigs))

if __name__ == '__main__':
    main()

