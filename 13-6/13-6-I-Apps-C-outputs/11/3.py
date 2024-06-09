
def preorder_traversal(tree):
    if tree:
        yield tree.val
        yield from preorder_traversal(tree.left)
        yield from preorder_traversal(tree.right)

def construct_tree(levels):
    if levels == 0:
        return None
    tree = TreeNode(1)
    queue = [tree]
    for i in range(1, 2**levels):
        if i % 2 == 0:
            queue[0].left = TreeNode(i+1)
            queue.append(queue[0].left)
        else:
            queue[0].right = TreeNode(i+1)
            queue.append(queue[0].right)
        queue.pop(0)
    return tree

def solve(levels):
    tree = construct_tree(levels)
    return ' '.join(map(str, preorder_traversal(tree)))

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

if __name__ == '__main__':
    levels = int(input())
    print(solve(levels))

