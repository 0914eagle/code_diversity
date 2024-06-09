
def f1(N):
    # Initialize the tree with the root node
    tree = [1]
    
    # Iterate through the levels
    for level in range(1, N):
        # Get the current level of the tree
        current_level = tree[:(2**level)]
        
        # Iterate through the current level
        for i in range(0, len(current_level), 2):
            # Calculate the sum of the left subtree
            left_sum = sum(current_level[i:i+1])
            
            # Calculate the sum of the right subtree
            right_sum = sum(current_level[i+1:i+2])
            
            # Calculate the difference between the two sums
            diff = abs(left_sum - right_sum)
            
            # Add the missing number to the tree
            tree.append(diff + 1)
    
    return tree

def f2(tree):
    # Return the tree in the preorder traversal
    return " ".join(str(x) for x in tree)

if __name__ == '__main__':
    N = int(input())
    tree = f1(N)
    print(f2(tree))

