
def read_input():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    return n, m, corridors

def find_cycles(n, corridors):
    visited = [False] * (n + 1)
    cycles = []
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i, visited, corridors, cycle)
            if len(cycle) > 1:
                cycles.append(cycle)
    return cycles

def dfs(i, visited, corridors, cycle):
    visited[i] = True
    cycle.append(i)
    for j, k in corridors:
        if i == j and not visited[k]:
            dfs(k, visited, corridors, cycle)
    return

def remove_cycles(n, m, corridors):
    cycles = find_cycles(n, corridors)
    removed_corridors = []
    for cycle in cycles:
        for i in range(1, len(cycle)):
            u, v = cycle[i - 1], cycle[i]
            removed_corridors.append((u, v))
    return removed_corridors

def main():
    n, m, corridors = read_input()
    removed_corridors = remove_cycles(n, m, corridors)
    print(len(removed_corridors))
    for u, v in removed_corridors:
        print(u, v)

if __name__ == '__main__':
    main()

