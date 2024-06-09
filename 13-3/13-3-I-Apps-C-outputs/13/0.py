
import sys
import math

def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, a, b, edges

def get_connected_components(n, edges):
    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            dfs(i, visited, edges, component)
            components.append(component)
    return components

def dfs(i, visited, edges, component):
    visited[i] = True
    component.append(i)
    for j, k in edges:
        if j == i and not visited[k]:
            dfs(k, visited, edges, component)
        elif k == i and not visited[j]:
            dfs(j, visited, edges, component)

def get_score(components, b):
    score = 0
    for component in components:
        component_score = 0
        for i in component:
            component_score += b[i - 1]
        score += abs(component_score)
    return score

def get_cost(components, a):
    cost = 0
    for component in components:
        for i in component:
            cost += a[i - 1]
    return cost

def get_profit(score, cost):
    return score - cost

def main():
    n, m, a, b, edges = get_input()
    components = get_connected_components(n, edges)
    score = get_score(components, b)
    cost = get_cost(components, a)
    profit = get_profit(score, cost)
    print(profit)

if __name__ == '__main__':
    main()

