
def count_ways_to_paint_tree(n, k, edges):
    # Initialize a dictionary to store the number of ways to paint each vertex
    ways = {i: 1 for i in range(1, n + 1)}
    
    # Iterate over the edges of the tree
    for u, v in edges:
        # If the distance between the two vertices is less than or equal to k,
        # then the number of ways to paint the two vertices is the product of the number of ways to paint each vertex
        if u != v and abs(u - v) <= k:
            ways[u] *= ways[v]
            ways[v] = ways[u]
    
    # Return the number of ways to paint the tree modulo 10^9 + 7
    return ways[1] % (10**9 + 7)

def main():
    n, k = map(int, input().split())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(count_ways_to_paint_tree(n, k, edges))

if __name__ == '__main__':
    main()

