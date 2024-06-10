
def get_layout(n, m):
    # Initialize the layout as a directed graph with n rooms and m corridors
    layout = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        layout[u].append(v)
    return layout

def get_cycles(layout):
    # Find all cycles in the layout
    cycles = []
    for i in range(1, len(layout)):
        for j in range(i + 1, len(layout)):
            if j in layout[i]:
                cycles.append((i, j))
    return cycles

def remove_cycles(layout, cycles):
    # Remove the cycles from the layout
    for cycle in cycles:
        u, v = cycle
        layout[u].remove(v)
        layout[v].remove(u)
    return layout

def get_removed_corridors(layout, cycles):
    # Get the indices of the removed corridors
    removed_corridors = []
    for i, room in enumerate(layout):
        for corridor in room:
            if (i + 1, corridor) in cycles:
                removed_corridors.append(i + 1)
                break
    return removed_corridors

def main():
    n, m = map(int, input().split())
    layout = get_layout(n, m)
    cycles = get_cycles(layout)
    removed_corridors = get_removed_corridors(layout, cycles)
    print(len(removed_corridors))
    print(*removed_corridors)

if __name__ == '__main__':
    main()

