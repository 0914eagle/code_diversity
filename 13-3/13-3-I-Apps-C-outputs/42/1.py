
def solve(N):
    nodes = [i for i in range(1, 2**N)]
    root = nodes[0]
    tree = [root]
    for i in range(1, N):
        left = []
        right = []
        for j in range(0, len(nodes), 2):
            if j + 1 < len(nodes):
                left.append(nodes[j])
                right.append(nodes[j+1])
        tree.extend(left)
        tree.extend(right)
        nodes = left + right
    return " ".join(map(str, tree))

