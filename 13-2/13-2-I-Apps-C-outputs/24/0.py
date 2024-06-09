
def create_bst(sequence):
    root = None
    for num in sequence:
        root = insert(root, num)
    return root

def insert(root, num):
    if root is None:
        return Node(num)
    if num < root.val:
        root.left = insert(root.left, num)
    else:
        root.right = insert(root.right, num)
    return root

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_depth(root):
    if root is None:
        return 0
    return 1 + max(get_depth(root.left), get_depth(root.right))

def main():
    n = int(input())
    sequence = [int(input()) for _ in range(n)]
    root = create_bst(sequence)
    print(get_depth(root))

if __name__ == '__main__':
    main()

