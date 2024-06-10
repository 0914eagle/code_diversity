
def get_input():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    return n, m, corridors

def find_cycles(n, corridors):
    visited = [False] * (n + 1)
    stack = []
    cycles = []
    for i in range(1, n + 1):
        if visited[i]:
            continue
        stack.append(i)
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            for neighbor in corridors:
                if neighbor[0] == node:
                    stack.append(neighbor[1])
                    break
            else:
                cycles.append(node)
    return cycles

def remove_cycles(n, m, corridors, cycles):
    removed_corridors = set()
    for cycle in cycles:
        for corridor in corridors:
            if corridor[0] == cycle or corridor[1] == cycle:
                removed_corridors.add(corridor)
    return removed_corridors

def main():
    n, m, corridors = get_input()
    cycles = find_cycles(n, corridors)
    removed_corridors = remove_cycles(n, m, corridors, cycles)
    print(len(removed_corridors))
    for corridor in removed_corridors:
        print(corridor)

if __name__ == '__main__':
    main()

