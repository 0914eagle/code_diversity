
def solve(N, edges):
    # Initialize the number of ways to divide the vertices into pairs as 0
    ways = 0
    
    # Iterate over all possible pairs of vertices
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            # Check if the shortest path between the two vertices contains all the edges
            if all(edge in edges for edge in [(i, j), (j, i)]):
                # Increment the number of ways to divide the vertices into pairs
                ways += 1
    
    # Return the result modulo 10^9 + 7
    return ways % 1000000007

def main():
    # Read the number of vertices and edges from stdin
    N = int(input())
    edges = []
    for _ in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    
    # Call the solve function and print the result
    print(solve(N, edges))

if __name__ == '__main__':
    main()

