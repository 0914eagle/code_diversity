
def calculate_probability(n, nodes):
    MOD = 10**9 + 7

    def dfs(node):
        nonlocal nodes_prob
        if node not in nodes_prob:
            return 1
        total_prob = 1
        for child in nodes_prob[node]:
            total_prob *= dfs(child)
            total_prob %= MOD
        return total_prob

    nodes_prob = {}
    for b, p in nodes:
        if p not in nodes_prob:
            nodes_prob[p] = []
        nodes_prob[p].append((b, p))

    return dfs(0)

if __name__ == '__main__':
    n = int(input())
    nodes = [list(map(int, input().split())) for _ in range(n)]
    result = calculate_probability(n, nodes)
    print(result)
