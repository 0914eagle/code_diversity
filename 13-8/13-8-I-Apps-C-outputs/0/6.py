
def is_possible(n, edges):
    # Initialize a dictionary to store the values on each edge
    values = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and update the values on each edge
    for u, v in edges:
        values[u] += values[v]
        values[v] += values[u]
    
    # Check if all values are equal
    return all(values[i] == values[1] for i in range(1, n + 1))

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("YES") if is_possible(n, edges) else print("NO")

if __name__ == '__main__':
    main()

