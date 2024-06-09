
def get_adjacent_island(island, n):
    if island == 0:
        return n - 1
    else:
        return island - 1

def get_empty_island(statues):
    for i in range(len(statues)):
        if statues[i] == 0:
            return i
    return -1

def can_rearrange_statues(n, statues, desired_statues):
    empty_island = get_empty_island(statues)
    if empty_island == -1:
        return "NO"
    while empty_island != 0:
        adjacent_island = get_adjacent_island(empty_island, n)
        if statues[adjacent_island] != desired_statues[empty_island]:
            return "NO"
        empty_island = adjacent_island
    return "YES"

if __name__ == '__main__':
    n = int(input())
    statues = list(map(int, input().split()))
    desired_statues = list(map(int, input().split()))
    print(can_rearrange_statues(n, statues, desired_statues))

