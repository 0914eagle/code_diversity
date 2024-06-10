
def is_possible_to_jump(grid, k, current_position):
    n = len(grid)
    if current_position == n-1:
        return True
    if current_position + k > n-1:
        return False
    if grid[current_position + k] == '#':
        return False
    return is_possible_to_jump(grid, k, current_position + k)

def is_target_reachable(grid, k):
    n = len(grid)
    for i in range(n):
        if grid[i] == 'G':
            if is_possible_to_jump(grid, k, i):
                return True
    return False

def main():
    n, k = map(int, input().split())
    grid = list(input())
    print("YES") if is_target_reachable(grid, k) else print("NO")

if __name__ == '__main__':
    main()

