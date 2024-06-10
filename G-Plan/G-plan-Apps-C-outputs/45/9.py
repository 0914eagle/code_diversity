
def calculate_probability(n, nodes):
    MOD = 10**9 + 7

    def dfs(node):
        if not node.children:
            return 1

        total_ways = 1
        for child in node.children:
            total_ways *= dfs(child)

        return total_ways % MOD

    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []

    tree = [Node(nodes[i][0]) for i in range(n)]
    for i in range(1, n):
        parent = nodes[i][1] - 1
        tree[parent].children.append(tree[i])

    probability = dfs(tree[0])
    return probability

if __name__ == '__main__':
    n = int(input())
    nodes = [list(map(int, input().split())) for _ in range(n)]
    result = calculate_probability(n, nodes)
    print(result)
