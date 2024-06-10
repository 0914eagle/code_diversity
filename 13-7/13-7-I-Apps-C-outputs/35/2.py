
def count_ways(N, edges):
    # Initialize a dictionary to store the number of ways to divide the vertices into pairs
    ways = {1: 1}
    
    # Iterate over the edges
    for i in range(N - 1):
        # Get the current edge
        u, v = edges[i]
        
        # If the number of ways to divide the vertices into pairs for the current edge is not already known
        if u not in ways or v not in ways:
            # Calculate the number of ways to divide the vertices into pairs for the current edge
            ways[u] = (ways[u] if u in ways else 1) * (ways[v] if v in ways else 1)
        else:
            # If the number of ways to divide the vertices into pairs for the current edge is already known,
            # update the number of ways to divide the vertices into pairs for the current edge
            ways[u] += ways[v]
    
    # Return the number of ways to divide the vertices into pairs that satisfy the condition, modulo 10^9 + 7
    return ways[1] % (10**9 + 7)

def main():
    # Read the number of vertices and edges from standard input
    N = int(input())
    edges = []
    for _ in range(N - 1):
        edges.append(tuple(map(int, input().split())))
    
    # Call the count_ways function to count the number of ways to divide the vertices into pairs that satisfy the condition
    print(count_ways(N, edges))

if __name__ == '__main__':
    main()

