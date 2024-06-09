
def get_statue_positions(n, a, b):
    # Initialize a dictionary to store the current position of each statue
    statue_positions = {}
    for i in range(n):
        if a[i] != 0:
            statue_positions[a[i]] = i
    return statue_positions

def get_empty_island(n, a):
    # Find the island with no statue
    for i in range(n):
        if a[i] == 0:
            return i
    return -1

def is_valid_move(n, statue_positions, empty_island, desired_statue):
    # Check if the move is valid
    if desired_statue == 0:
        return True
    if desired_statue not in statue_positions:
        return False
    current_position = statue_positions[desired_statue]
    if abs(current_position - empty_island) > 1:
        return False
    return True

def can_rearrange_statues(n, a, b):
    # Get the current positions of the statues
    statue_positions = get_statue_positions(n, a, b)
    empty_island = get_empty_island(n, a)
    # Check if the desired statues can be rearranged
    for i in range(n):
        if not is_valid_move(n, statue_positions, empty_island, b[i]):
            return False
    return True

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES") if can_rearrange_statues(n, a, b) else print("NO")

if __name__ == '__main__':
    main()

