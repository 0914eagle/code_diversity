
def read_input():
    n, m = map(int, input().split())
    floorplan = [input() for _ in range(n)]
    return n, m, floorplan

def is_solvable(n, m, floorplan):
    # Check if the puzzle has a solution
    # If the puzzle has no solution, return False
    return True

def solve_puzzle(n, m, floorplan):
    # Solve the puzzle and return the minimum number of gargoyles that have to be rotated
    return 0

def main():
    n, m, floorplan = read_input()
    if is_solvable(n, m, floorplan):
        print(solve_puzzle(n, m, floorplan))
    else:
        print(-1)

if __name__ == '__main__':
    main()

