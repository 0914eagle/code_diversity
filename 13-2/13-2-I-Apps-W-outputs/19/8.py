
def count_ways_to_paint_tree(n, k, edges):
    # Initialize a list to store the number of ways to paint each vertex
    ways = [1] * n
    for i in range(n):
        # For each vertex, count the number of ways to paint its neighbors
        for j in range(n):
            if i != j and edges[i][j] == 1:
                ways[i] = (ways[i] + ways[j]) % 1000000007
    # Return the number of ways to paint the tree
    return ways[0]

def main():
    n, k = map(int, input().split())
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append([u, v])
    print(count_ways_to_paint_tree(n, k, edges))

if __name__ == '__main__':
    main()

