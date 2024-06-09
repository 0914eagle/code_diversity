
def get_maximum_gold(n, m, roads, gold):
    # Initialize a graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize a dictionary to store the maximum gold that can be stolen from each village
    max_gold = {1: 0}
    
    # Function to recursively find the maximum gold that can be stolen from a village
    def dfs(village):
        nonlocal max_gold
        if village not in max_gold:
            max_gold[village] = 0
            for neighbor in graph[village]:
                dfs(neighbor)
            max_gold[village] = max(max_gold[village], gold[village] + max_gold[neighbor])
    
    # Call the dfs function for the bandit's home village
    dfs(1)
    
    # Return the maximum gold that can be stolen from the bandit's home village
    return max_gold[1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    gold = []
    for _ in range(n - 2):
        a, b = map(int, input().split())
        roads.append((a, b))
        gold.append(int(input()))
    print(get_maximum_gold(n, m, roads, gold))

