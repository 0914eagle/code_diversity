
def get_empty_island(statues):
    for i, statue in enumerate(statues):
        if statue == 0:
            return i
    return -1

def get_next_island(empty_island, desired_statues, current_statues):
    for i in range(len(desired_statues)):
        if desired_statues[i] == current_statues[empty_island]:
            return i
    return -1

def can_arrange_statues(statues, desired_statues):
    empty_island = get_empty_island(statues)
    if empty_island == -1:
        return False
    current_statues = statues[:]
    while empty_island != -1:
        next_island = get_next_island(empty_island, desired_statues, current_statues)
        if next_island == -1:
            return False
        current_statues[empty_island] = current_statues[next_island]
        current_statues[next_island] = 0
        empty_island = get_empty_island(current_statues)
    return True

if __name__ == '__main__':
    n = int(input())
    statues = list(map(int, input().split()))
    desired_statues = list(map(int, input().split()))
    print("YES" if can_arrange_statues(statues, desired_statues) else "NO")

