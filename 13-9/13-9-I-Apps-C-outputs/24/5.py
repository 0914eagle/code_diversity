
def get_tree(n, cs):
    # Base case: if n is 1, return a single node
    if n == 1:
        return [1]
    
    # Initialize an empty tree
    tree = []
    
    # Iterate over all possible root nodes
    for i in range(1, n + 1):
        # If the root node has at least two sons, recursively build the left and right subtrees
        if i < n and cs[i] >= 2:
            left_subtree = get_tree(i - 1, cs[:i])
            right_subtree = get_tree(n - i, cs[i:])
            # If both subtrees are valid, combine them into a single tree
            if left_subtree and right_subtree:
                tree.append(i)
                tree.extend(left_subtree)
                tree.extend(right_subtree)
                break
    
    # If no valid tree was found, return None
    if not tree:
        return None
    
    # If the tree is valid, return it
    return tree

def is_valid_tree(n, cs):
    # Get the rooted tree
    tree = get_tree(n, cs)
    
    # If the tree is None, return False
    if not tree:
        return False
    
    # If the tree is valid, return True
    return True

def main():
    n = int(input())
    cs = list(map(int, input().split()))
    print("YES") if is_valid_tree(n, cs) else print("NO")

if __name__ == '__main__':
    main()

