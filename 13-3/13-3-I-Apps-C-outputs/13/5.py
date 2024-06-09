
import sys
import math

def get_graph():
    n, m = map(int, input().split())
    graph = {}
    for i in range(n):
        graph[i+1] = []
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    return graph

def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def get_connected_components(graph):
    visited = [False] * (len(graph) + 1)
    components = []
    for node in graph:
        if not visited[node]:
            component = []
            dfs(graph, node, visited)
            for node in graph:
                if visited[node]:
                    component.append(node)
            components.append(component)
    return components

def get_score(graph, components):
    score = 0
    for component in components:
        component_score = 0
        for node in component:
            component_score += graph[node][1]
        score += abs(component_score)
    return score

def get_cost(graph, vertices):
    cost = 0
    for vertex in vertices:
        cost += graph[vertex][0]
    return cost

def get_profit(graph, components, vertices):
    score = get_score(graph, components)
    cost = get_cost(graph, vertices)
    return score - cost

def f1(...):
    ...
    return ...

def f2(...):
    ...
    return ...

if __name__ == '__main__':
    graph = get_graph()
    components = get_connected_components(graph)
    vertices = [1, 2, 3, 4]
    profit = get_profit(graph, components, vertices)
    print(profit)

