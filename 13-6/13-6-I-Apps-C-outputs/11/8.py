
def get_preorder_traversal(tree):
    
    if not tree:
        return []
    return [tree[0]] + get_preorder_traversal(tree[1]) + get_preorder_traversal(tree[2])

def build_tree(N):
    
    if N == 1:
        return [1]
    else:
        return [0] + build_tree(N-1) + build_tree(N-1)

def solve(N):
    
    tree = build_tree(N)
    return get_preorder_traversal(tree)

if __name__ == '__main__':
    N = int(input())
    print(*solve(N))

