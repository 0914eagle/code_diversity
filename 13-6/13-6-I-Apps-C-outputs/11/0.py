
def preorder_traversal(tree):
    if not tree:
        return []
    return [tree.val] + preorder_traversal(tree.left) + preorder_traversal(tree.right)

def build_tree(N):
    if N == 0:
        return None
    tree = TreeNode(N)
    tree.left = build_tree(N-1)
    tree.right = build_tree(N-1)
    return tree

def solve(N):
    tree = build_tree(N)
    return preorder_traversal(tree)

if __name__ == '__main__':
    N = int(input())
    print(*solve(N))

