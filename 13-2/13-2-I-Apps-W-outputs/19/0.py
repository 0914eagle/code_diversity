
def count_ways_to_paint_tree(n, k, edges):
    # Initialize a list to store the number of ways to paint each vertex
    ways = [1] * n

    # Iterate over the edges and update the number of ways to paint each vertex
    for u, v in edges:
        ways[u - 1] = (ways[u - 1] + ways[v - 1]) % 1000000007

    # Return the number of ways to paint the tree
    return ways[0]

def main():
    n, k = map(int, input().split())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(count_ways_to_paint_tree(n, k, edges))

if __name__ == '__main__':
    main()

