
def get_cycles(n, m, corridors):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in corridors:
        graph[u-1].append(v-1)
    
    # Find all cycles in the graph
    cycles = []
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] == 1:
                cycles.append([i+1, j+1])
    
    return cycles

def remove_corridors(n, m, corridors, k):
    # Initialize a set to keep track of removed corridors
    removed = set()
    
    # Remove at most k corridors
    for i in range(k):
        # Find the longest cycle
        longest_cycle = None
        for cycle in get_cycles(n, m, corridors):
            if longest_cycle is None or len(cycle) > len(longest_cycle):
                longest_cycle = cycle
        
        # Remove the first edge in the cycle
        u, v = longest_cycle[0], longest_cycle[1]
        removed.add((u, v))
        corridors.remove((u, v))
    
    return removed

def main():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    
    # Remove at most half of the corridors
    removed = remove_corridors(n, m, corridors, m//2)
    
    # Print the number of removed corridors
    print(len(removed))
    
    # Print the removed corridors
    for u, v in removed:
        print(u, v)

if __name__ == '__main__':
    main()

