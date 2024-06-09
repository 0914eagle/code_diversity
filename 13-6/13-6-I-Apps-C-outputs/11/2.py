
def f1(N):
    # create a list to store the numbers 1 to 2^N - 1
    numbers = list(range(1, 2**N))
    # create an empty list to store the preorder traversal of the tree
    preorder = []
    # call the recursive function to build the tree
    build_tree(numbers, preorder, 0)
    # return the preorder traversal of the tree
    return " ".join(map(str, preorder))

def build_tree(numbers, preorder, level):
    # if there are no more numbers to assign, return
    if not numbers:
        return
    # if this is the last level, assign the next number to the current node and return
    if level == N - 1:
        preorder.append(numbers.pop(0))
        return
    # recursively build the left and right subtrees
    build_tree(numbers, preorder, level + 1)
    build_tree(numbers, preorder, level + 1)
    # assign the next number to the current node
    preorder.append(numbers.pop(0))

if __name__ == '__main__':
    N = int(input())
    print(f1(N))

