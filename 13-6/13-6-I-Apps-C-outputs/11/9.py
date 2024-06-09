
def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def fill_tree(root, values, level):
    if root is None:
        return
    if level == 0:
        root.val = values[0]
        values = values[1:]
    else:
        fill_tree(root.left, values, level-1)
        fill_tree(root.right, values, level-1)
        root.val = root.left.val + root.right.val

def solve(N):
    values = list(range(1, 2**N))
    root = Node(None)
    fill_tree(root, values, N-1)
    return preorder_traversal(root)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

if __name__ == '__main__':
    N = int(input())
    print(*solve(N))

