
def calculate_probability(n, nodes):
    MOD = 10**9 + 7

    def dfs(node):
        if not node.children:
            return 1

        total_ways = 1
        for child in node.children:
            total_ways = (total_ways * dfs(child)) % MOD

        return total_ways

    class Node:
        def __init__(self, b):
            self.b = b
            self.children = []

    tree = [Node(b) for b, _ in nodes]
    for i, (_, parent) in enumerate(nodes):
        if parent != 0:
            tree[parent - 1].children.append(tree[i])

    root = tree[0]
    total_ways = dfs(root)
    return total_ways % MOD

if __name__ == '__main__':
    n = int(input())
    nodes = [tuple(map(int, input().split())) for _ in range(n)]
    result = calculate_probability(n, nodes)
    print(result)
