
def get_statue_position(statue_list, island_index):
    return statue_list[island_index - 1]

def get_empty_island_index(statue_list):
    return statue_list.index(0)

def can_move_statue(statue_list, island_index):
    empty_island_index = get_empty_island_index(statue_list)
    if empty_island_index == island_index:
        return False
    if empty_island_index == island_index - 1:
        return True
    if empty_island_index == island_index + 1:
        return True
    return False

def move_statue(statue_list, island_index):
    empty_island_index = get_empty_island_index(statue_list)
    statue_list[empty_island_index] = get_statue_position(statue_list, island_index)
    statue_list[island_index - 1] = 0
    return statue_list

def is_desired_order(statue_list, desired_order):
    return statue_list == desired_order

def solve_puzzle(statue_list, desired_order):
    if is_desired_order(statue_list, desired_order):
        return "YES"
    for island_index in range(1, len(statue_list) + 1):
        if can_move_statue(statue_list, island_index):
            statue_list = move_statue(statue_list, island_index)
            if is_desired_order(statue_list, desired_order):
                return "YES"
    return "NO"

if __name__ == '__main__':
    n = int(input())
    statue_list = list(map(int, input().split()))
    desired_order = list(map(int, input().split()))
    print(solve_puzzle(statue_list, desired_order))

