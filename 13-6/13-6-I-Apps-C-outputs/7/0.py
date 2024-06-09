
import sys
import itertools

def get_input():
    n, k = map(int, input().split())
    courses = []
    for _ in range(n):
        name, diff = input().split()
        courses.append((name, int(diff)))
    return n, k, courses

def f1(n, k, courses):
    # create a graph with courses as nodes and edges between courses with the same name but different levels
    graph = [[] for _ in range(n)]
    for i, (name, _) in enumerate(courses):
        for j, (name2, _) in enumerate(courses):
            if name == name2 and i != j:
                graph[i].append(j)
    
    # find the shortest path in the graph with at most k nodes
    visited = [False] * n
    queue = [(0, 0, [])]
    while queue:
        dist, node, path = heapq.heappop(queue)
        if len(path) == k:
            return dist
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(queue, (dist + courses[neighbor][1], neighbor, path + [neighbor]))
    
    return -1

def f2(n, k, courses):
    # create a graph with courses as nodes and edges between courses with the same name but different levels
    graph = [[] for _ in range(n)]
    for i, (name, _) in enumerate(courses):
        for j, (name2, _) in enumerate(courses):
            if name == name2 and i != j:
                graph[i].append(j)
    
    # find the minimum spanning tree in the graph
    parent = [-1] * n
    rank = [0] * n
    for i in range(n):
        if parent[i] == -1:
            dfs(i, -1, graph, parent, rank)
    
    # find the shortest path in the minimum spanning tree with at most k nodes
    visited = [False] * n
    queue = [(0, 0, [])]
    while queue:
        dist, node, path = heapq.heappop(queue)
        if len(path) == k:
            return dist
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor] and parent[neighbor] == node:
                heapq.heappush(queue, (dist + courses[neighbor][1], neighbor, path + [neighbor]))
    
    return -1

def dfs(node, parent, graph, parent_list, rank_list):
    parent_list[node] = parent
    rank_list[node] = 0
    for neighbor in graph[node]:
        if parent_list[neighbor] == -1:
            dfs(neighbor, node, graph, parent_list, rank_list)
            rank_list[node] = max(rank_list[node], rank_list[neighbor] + 1)

if __name__ == '__main__':
    n, k, courses = get_input()
    print(f1(n, k, courses))
    print(f2(n, k, courses))

