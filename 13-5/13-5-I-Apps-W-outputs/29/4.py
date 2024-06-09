
def solve(n, m, a, b, roads):
    # Initialize a graph to store the roads
    graph = [[] for _ in range(n)]
    for p, q in roads:
        graph[p-1].append(q-1)
        graph[q-1].append(p-1)
    
    # Initialize an array to store the number of soldiers in each city
    soldiers = [0] * n
    for i in range(n):
        soldiers[i] = a[i]
    
    # Loop through each city and check if the number of soldiers is correct
    for i in range(n):
        if soldiers[i] != b[i]:
            return "NO"
    
    return "YES"

