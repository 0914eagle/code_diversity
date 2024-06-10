
def count_pairs(n, a, p):
    # Initialize a dictionary to store the number of apples on each node
    apples = {i: a[i-1] for i in range(1, n+1)}
    # Initialize a dictionary to store the parent of each node
    parents = {i: p[i-1] for i in range(1, n+1)}
    # Initialize a set to store the pairs of nodes that can be swapped
    pairs = set()
    # Iterate over all pairs of nodes
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # If the nodes are not the same and have different parity, they can be swapped
            if i != j and (i % 2) != (j % 2):
                pairs.add((i, j))
    return len(pairs)

def solve(n, a, p):
    # Call the count_pairs function to count the number of pairs of nodes that can be swapped
    count = count_pairs(n, a, p)
    # Print the number of pairs
    print(count)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    solve(n, a, p)

