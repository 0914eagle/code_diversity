
def get_swap_pairs(n, apples, parents):
    # Initialize a dictionary to store the number of apples on each node
    node_apples = {i: apples[i-1] for i in range(1, n+1)}
    # Initialize a set to store the pairs of nodes that can be swapped
    swap_pairs = set()
    
    # Iterate over the nodes in the tree
    for i in range(1, n+1):
        # If the node is a leaf, skip it
        if i == n or node_apples[i] == 0:
            continue
        # If the node has only one child, skip it
        if len(parents[i-1]) == 1:
            continue
        # If the node has two children, find the pairs of nodes that can be swapped
        for j in parents[i-1]:
            for k in parents[i-1]:
                if j != k:
                    swap_pairs.add((i, j))
                    swap_pairs.add((i, k))
    
    return len(swap_pairs)

def main():
    n = int(input())
    apples = list(map(int, input().split()))
    parents = [[] for _ in range(n)]
    for i in range(1, n):
        parents[int(input())-1].append(i)
    print(get_swap_pairs(n, apples, parents))

if __name__ == '__main__':
    main()

