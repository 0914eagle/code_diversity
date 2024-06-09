
def f1(N):
    # Calculate the total number of nodes in the tree
    total_nodes = 2**N - 1
    
    # Create a list to store the numbers
    numbers = list(range(1, total_nodes+1))
    
    # Create a list to store the tree
    tree = []
    
    # Call the recursive function to build the tree
    build_tree(numbers, tree, N)
    
    # Return the tree in the preorder traversal
    return " ".join(map(str, tree))

def build_tree(numbers, tree, level):
    # Base case: if there are no more numbers, return
    if not numbers:
        return
    
    # Get the first number from the list
    num = numbers.pop(0)
    
    # Add the number to the tree
    tree.append(num)
    
    # If we are not at the last level, recursively call the function to build the left and right subtrees
    if level > 1:
        build_tree(numbers, tree, level-1)
        build_tree(numbers, tree, level-1)

if __name__ == '__main__':
    N = int(input())
    print(f1(N))

