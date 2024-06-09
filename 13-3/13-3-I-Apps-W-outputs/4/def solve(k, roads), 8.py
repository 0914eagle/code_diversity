
def solve(k, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, 2*k+1)}
    for a, b, t in roads:
        graph[a].add((b, t))
        graph[b].add((a, t))
    
    # Find the minimum sum by trying all possible assignments
    min_sum = float('inf')
    for assignment in itertools.permutations(range(1, 2*k+1), 2*k):
        sum_f = 0
        for i in range(k):
            a, b = assignment[i], assignment[i+k]
            for c, t in graph[a]:
                if c == b:
                    sum_f += t
                    break
        if sum_f < min_sum:
            min_sum = sum_f
    
    # Find the maximum sum by trying all possible assignments
    max_sum = 0
    for assignment in itertools.permutations(range(1, 2*k+1), 2*k):
        sum_f = 0
        for i in range(k):
            a, b = assignment[i], assignment[i+k]
            for c, t in graph[a]:
                if c == b:
                    sum_f += t
                    break
        if sum_f > max_sum:
            max_sum = sum_f
    
    return min_sum, max_sum

