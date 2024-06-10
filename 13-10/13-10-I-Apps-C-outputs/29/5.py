
import heapq
import sys
import math

def dijkstra(graph, start, visited):
    queue = []
    heapq.heappush(queue, (0, start))
    visited[start] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if node == graph[-1]:
            return dist
        for neighbor, weight in graph[node]:
            if visited[neighbor] > dist + weight:
                visited[neighbor] = dist + weight
                heapq.heappush(queue, (dist + weight, neighbor))
    return float("inf")

def get_min_distance(graph, start, visited):
    queue = []
    heapq.heappush(queue, (0, start))
    visited[start] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if node == graph[-1]:
            return dist
        for neighbor, weight in graph[node]:
            if visited[neighbor] > dist + weight:
                visited[neighbor] = dist + weight
                heapq.heappush(queue, (dist + weight, neighbor))
    return float("inf")

def get_town_spring_dist(n, s, t, q, hills, springs, towns):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            xi, yi, hi = hills[i]
            xj, yj, hj = hills[j]
            dist = math.sqrt((xi-xj)**2 + (yi-yj)**2)
            if hi < hj:
                graph[i].append((j, dist))
            else:
                graph[j].append((i, dist))
    visited = [float("inf") for _ in range(n)]
    distance = 0
    for i in range(t):
        spring = springs[i]
        town = towns[i]
        distance += dijkstra(graph, town, visited)
    return distance

def get_spring_spring_dist(n, s, t, q, hills, springs, towns):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            xi, yi, hi = hills[i]
            xj, yj, hj = hills[j]
            dist = math.sqrt((xi-xj)**2 + (yi-yj)**2)
            if hi < hj:
                graph[i].append((j, dist))
            else:
                graph[j].append((i, dist))
    visited = [float("inf") for _ in range(n)]
    distance = 0
    for i in range(s):
        for j in range(i+1, s):
            spring_i = springs[i]
            spring_j = springs[j]
            distance += get_min_distance(graph, spring_i, visited) + get_min_distance(graph, spring_j, visited)
    return distance

def get_total_dist(n, s, t, q, hills, springs, towns):
    return get_town_spring_dist(n, s, t, q, hills, springs, towns) + get_spring_spring_dist(n, s, t, q, hills, springs, towns)

def main():
    n, s, t, q = map(int, input().split())
    hills = []
    for i in range(n):
        x, y, h = map(int, input().split())
        hills.append((x, y, h))
    springs = list(map(int, input().split()))
    towns = list(map(int, input().split()))
    print(get_total_dist(n, s, t, q, hills, springs, towns))

if __name__ == '__main__':
    main()

