
def f1(N, edges):
    # Initialize the number of ways to divide the vertices into pairs as 0
    ways = 0
    
    # Iterate over all possible pairs of vertices
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            # Check if there is an edge between the two vertices
            if (i, j) in edges or (j, i) in edges:
                # Increment the number of ways to divide the vertices into pairs
                ways += 1
    
    # Return the number of ways to divide the vertices into pairs modulo 10^9 + 7
    return ways % 1000000007

def f2(N, edges):
    # Initialize the number of ways to divide the vertices into pairs as 0
    ways = 0
    
    # Iterate over all possible pairs of vertices
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            # Check if there is an edge between the two vertices
            if (i, j) in edges or (j, i) in edges:
                # Increment the number of ways to divide the vertices into pairs
                ways += 1
    
    # Return the number of ways to divide the vertices into pairs modulo 10^9 + 7
    return ways % 1000000007

if __name__ == '__main__':
    N = int(input())
    edges = []
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    print(f1(N, edges))
    print(f2(N, edges))

