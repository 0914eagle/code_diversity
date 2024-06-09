
def solve(N):
    nodes = [i for i in range(1, 2**N)]
    root = nodes[0]
    tree = [root]
    for i in range(1, N):
        left = nodes[i]
        right = nodes[-i]
        tree.append(left)
        tree.append(right)
    return " ".join(map(str, tree))

