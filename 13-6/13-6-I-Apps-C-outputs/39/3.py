
def get_empty_island(statues):
    for i, statue in enumerate(statues):
        if statue == 0:
            return i
    return -1

def get_statue_neighbors(island, statues):
    neighbors = []
    if island > 0:
        neighbors.append(island - 1)
    if island < len(statues) - 1:
        neighbors.append(island + 1)
    return neighbors

def can_rearrange_statues(statues, desired_statues):
    empty_island = get_empty_island(statues)
    if empty_island == -1:
        return False
    visited = set()
    queue = [(empty_island, [])]
    while queue:
        current_island, path = queue.pop(0)
        if current_island in visited:
            continue
        visited.add(current_island)
        if statues[current_island] == desired_statues[current_island]:
            return True
        for neighbor in get_statue_neighbors(current_island, statues):
            if neighbor not in visited:
                queue.append((neighbor, path + [current_island]))
    return False

def main():
    n = int(input())
    statues = list(map(int, input().split()))
    desired_statues = list(map(int, input().split()))
    print("YES") if can_rearrange_statues(statues, desired_statues) else print("NO")

if __name__ == '__main__':
    main()

