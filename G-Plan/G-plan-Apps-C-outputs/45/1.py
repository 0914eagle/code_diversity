
def calculate_probability(n, nodes):
    MOD = 10**9 + 7

    def dfs(node):
        if not children[node]:
            return 1

        total_ways = 1
        for child in children[node]:
            total_ways = (total_ways * dfs(child)) % MOD

        return total_ways

    children = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        parent = nodes[i][1]
        children[parent].append(i)

    probability = dfs(1)
    return probability

if __name__ == '__main__':
    n = int(input())
    nodes = {}
    for i in range(1, n + 1):
        b, p = map(int, input().split())
        nodes[i] = (b, p)

    result = calculate_probability(n, nodes)
    print(result)
