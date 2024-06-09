
def solve(N):
    # Initialize a list to store the numbers 1 to 2^N - 1
    numbers = list(range(1, 2**N))
    # Initialize an empty list to store the preorder traversal of the tree
    preorder = []
    # Recursively build the tree using the numbers list
    build_tree(numbers, preorder, 0, N)
    # Return the preorder traversal of the tree
    return " ".join(map(str, preorder))

def build_tree(numbers, preorder, level, N):
    # If there are no more numbers to assign, return
    if not numbers:
        return
    # If we have reached the last level, assign the first number and return
    if level == N - 1:
        preorder.append(numbers.pop(0))
        return
    # Otherwise, recursively build the left and right subtrees
    build_tree(numbers, preorder, level + 1, N)
    build_tree(numbers, preorder, level + 1, N)
    # Assign the current number to the root node
    preorder.append(numbers.pop(0))

print(solve(int(input())))

