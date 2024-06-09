
def solve(N):
    # Initialize a list to store the numbers 1 to 2^N - 1
    numbers = list(range(1, 2**N))
    # Initialize an empty list to store the preorder traversal of the tree
    preorder = []
    # Recursively build the tree using the numbers list
    build_tree(numbers, preorder, N)
    # Return the preorder traversal of the tree
    return " ".join(map(str, preorder))

def build_tree(numbers, preorder, level):
    # If there are no more numbers to assign, return
    if not numbers:
        return
    # If we are at the last level, assign the first number and return
    if level == 0:
        preorder.append(numbers.pop(0))
        return
    # Recursively build the left subtree
    build_tree(numbers, preorder, level - 1)
    # Recursively build the right subtree
    build_tree(numbers, preorder, level - 1)
    # Assign the current number to the current node
    preorder.append(numbers.pop(0))

N = int(input())
print(solve(N))

