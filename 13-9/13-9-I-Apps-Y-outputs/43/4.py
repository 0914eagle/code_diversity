
def get_roads(n, a):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]
    # Iterate over the districts and add them to the graph
    for i in range(n):
        graph[i].append(i)
    # Iterate over the districts and add them to the graph
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                graph[i].append(j)
                graph[j].append(i)
    # Return the graph
    return graph

def can_reach_all_districts(graph):
    # Initialize a set to keep track of visited districts
    visited = set()
    # Initialize a queue to keep track of districts to visit
    queue = [0]
    # Iterate until the queue is empty
    while queue:
        # Dequeue a district
        district = queue.pop(0)
        # If the district has not been visited, mark it as visited and add it to the set
        if district not in visited:
            visited.add(district)
            # Add the neighbors of the district to the queue
            queue += graph[district]
    # If all districts have been visited, return True, otherwise return False
    return len(visited) == len(graph)

def build_roads(n, a):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]
    # Iterate over the districts and add them to the graph
    for i in range(n):
        graph[i].append(i)
    # Iterate over the districts and add them to the graph
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                graph[i].append(j)
                graph[j].append(i)
    # Return the graph
    return graph

def main():
    # Read the number of test cases
    t = int(input())
    # Iterate over the test cases
    for _ in range(t):
        # Read the number of districts
        n = int(input())
        # Read the gangs of the districts
        a = list(map(int, input().split()))
        # Build the graph
        graph = build_roads(n, a)
        # Check if all districts are reachable
        if can_reach_all_districts(graph):
            print("YES")
            # Print the roads
            for i in range(n):
                for j in graph[i]:
                    if j > i:
                        print(i, j)
        else:
            print("NO")

if __name__ == '__main__':
    main()

