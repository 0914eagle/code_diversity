
def get_input():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    return n, m, corridors

def find_cycles(corridors):
    visited = set()
    cycles = []
    for u, v in corridors:
        if u not in visited:
            visited.add(u)
            dfs(u, v, visited, cycles)
    return cycles

def dfs(u, v, visited, cycles):
    if v not in visited:
        visited.add(v)
        for w in corridors:
            if w[0] == v:
                dfs(v, w[1], visited, cycles)
        cycles.append((u, v))

def remove_cycles(cycles):
    removed_corridors = []
    for cycle in cycles:
        removed_corridors.append(cycle[0])
    return removed_corridors

def main():
    n, m, corridors = get_input()
    cycles = find_cycles(corridors)
    removed_corridors = remove_cycles(cycles)
    print(len(removed_corridors))
    for corridor in removed_corridors:
        print(corridor)

if __name__ == '__main__':
    main()

