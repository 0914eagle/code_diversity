
def count_swap_ways(n, a, p):
    # Initialize a dictionary to store the number of apples on each node
    apples = {i: a[i-1] for i in range(1, n+1)}
    # Initialize a list to store the children of each node
    children = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        children[p[i-1]].append(i)
    # Initialize a set to store the nodes that are leaves
    leaves = set()
    for i in range(1, n+1):
        if not children[i]:
            leaves.add(i)
    # Initialize a set to store the nodes that are not leaves
    non_leaves = set(range(1, n+1)) - leaves
    # Initialize a list to store the number of ways to make the swap for each node
    swap_ways = [0] * (n+1)
    # Base case: if a node is a leaf, it can only be swapped with itself
    for i in leaves:
        swap_ways[i] = 1
    # Recursive case: if a node is not a leaf, it can be swapped with any of its children
    for i in non_leaves:
        for j in children[i]:
            swap_ways[i] += swap_ways[j]
    # Return the sum of the number of ways to make the swap for all nodes
    return sum(swap_ways)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(count_swap_ways(n, a, p))

if __name__ == '__main__':
    main()

