
def f1(N):
    # Calculate the number of nodes in the tree
    num_nodes = 2**N - 1
    
    # Create a list to store the numbers
    numbers = list(range(1, num_nodes+1))
    
    # Create a list to store the tree
    tree = []
    
    # Fill the tree with the numbers
    for i in range(num_nodes):
        tree.append(numbers[i])
    
    # Return the tree
    return tree

def f2(tree):
    # Calculate the number of levels in the tree
    num_levels = len(tree)
    
    # Create a list to store the sums of the left and right subtrees
    sums = [0] * num_levels
    
    # Fill the sums list with the sums of the left and right subtrees
    for i in range(num_levels):
        if i == 0:
            sums[i] = tree[i]
        else:
            sums[i] = sums[i-1] + tree[i]
    
    # Return the sums list
    return sums

def f3(tree, sums):
    # Calculate the number of levels in the tree
    num_levels = len(tree)
    
    # Create a list to store the differences between the sums of the left and right subtrees
    diffs = [0] * num_levels
    
    # Fill the diffs list with the differences between the sums of the left and right subtrees
    for i in range(num_levels):
        if i == 0:
            diffs[i] = abs(sums[i] - sums[i])
        else:
            diffs[i] = abs(sums[i] - sums[i-1])
    
    # Return the diffs list
    return diffs

def f4(tree, diffs):
    # Calculate the number of levels in the tree
    num_levels = len(tree)
    
    # Create a list to store the nodes at each level
    nodes = [[] for _ in range(num_levels)]
    
    # Fill the nodes list with the nodes at each level
    for i in range(num_levels):
        nodes[i].append(tree[i])
    
    # Return the nodes list
    return nodes

def f5(nodes):
    # Calculate the number of levels in the tree
    num_levels = len(nodes)
    
    # Create a list to store the output
    output = []
    
    # Fill the output list with the numbers in the tree
    for i in range(num_levels):
        for j in range(len(nodes[i])):
            output.append(nodes[i][j])
    
    # Return the output list
    return output

if __name__ == '__main__':
    # Get the number of levels from the user
    N = int(input())
    
    # Create the tree
    tree = f1(N)
    
    # Calculate the sums of the left and right subtrees
    sums = f2(tree)
    
    # Calculate the differences between the sums of the left and right subtrees
    diffs = f3(tree, sums)
    
    # Calculate the nodes at each level
    nodes = f4(tree, diffs)
    
    # Calculate the output
    output = f5(nodes)
    
    # Print the output
    print(*output)

