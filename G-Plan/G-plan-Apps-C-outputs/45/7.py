
def calculate_probability(n, nodes):
    MOD = 10**9 + 7

    def dfs(node):
        if not node.children:
            return 1

        total = 1
        for child in node.children:
            total *= dfs(child)
            total %= MOD

        return total

    class Node:
        def __init__(self, b):
            self.b = b
            self.children = []

    tree = [Node(b) for b, _ in nodes]
    for i, (_, parent) in enumerate(nodes[1:], start=1):
        tree[parent - 1].children.append(tree[i])

    probability = dfs(tree[0])
    return probability % MOD

if __name__ == '__main__':
    n = int(input())
    nodes = [list(map(int, input().split())) for _ in range(n)]
    result = calculate_probability(n, nodes)
    print(result)
