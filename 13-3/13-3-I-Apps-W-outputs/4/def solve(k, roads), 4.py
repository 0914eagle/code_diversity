
def solve(k, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, 2*k+1)}
    for a, b, t in roads:
        graph[a].add((b, t))
        graph[b].add((a, t))
    
    # Find the minimum sum by assigning each person to a house such that the sum of f(i) is minimized
    min_sum = float('inf')
    for assignment in itertools.permutations(range(1, 2*k+1)):
        sum_f = 0
        for i in range(k):
            person1, person2 = assignment[i], assignment[i+k]
            sum_f += find_shortest_path(graph, person1, person2)
        if sum_f < min_sum:
            min_sum = sum_f
    
    # Find the maximum sum by assigning each person to a house such that the sum of f(i) is maximized
    max_sum = 0
    for assignment in itertools.permutations(range(1, 2*k+1)):
        sum_f = 0
        for i in range(k):
            person1, person2 = assignment[i], assignment[i+k]
            sum_f += find_shortest_path(graph, person1, person2)
        if sum_f > max_sum:
            max_sum = sum_f
    
    return min_sum, max_sum

def find_shortest_path(graph, start, end):
    visited = set()
    queue = [(start, 0)]
    while queue:
        node, distance = queue.pop(0)
        if node == end:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                queue.append((neighbor, distance + weight))
    return 0

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        roads = []
        for _ in range(2*k-1):
            a, b, t = map(int, input().split())
            roads.append((a, b, t))
        print(*solve(k, roads))

