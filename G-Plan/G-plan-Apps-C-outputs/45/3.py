
def calculate_probability(n, nodes):
    MOD = 10**9 + 7
    
    def dfs(node, value):
        if not node:
            return 1, 1
        
        total, valid = 1, 1
        for child in nodes[node]:
            if nodes[child][0] < value:
                child_total, child_valid = dfs(child, nodes[child][0])
                total = (total * child_total) % MOD
                valid = (valid * child_valid) % MOD
            else:
                child_total, _ = dfs(child, nodes[child][0])
                total = (total * child_total) % MOD
        
        if value < nodes[node][0]:
            return total, (valid * pow(total, MOD - 2, MOD)) % MOD
        else:
            return total, 0
    
    return dfs(1, nodes[1][0])[1]


if __name__ == '__main__':
    n = int(input())
    nodes = {i: tuple(map(int, input().split())) for i in range(1, n + 1)}
    adjacency_list = {i: [] for i in range(1, n + 1)}
    
    for i in range(2, n + 1):
        parent = nodes[i][1]
        adjacency_list[parent].append(i)
    
    result = calculate_probability(n, nodes)
    print(result)
