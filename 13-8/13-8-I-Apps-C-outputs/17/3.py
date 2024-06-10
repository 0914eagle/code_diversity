
def get_input():
    n = int(input())
    vertical_spec = [list(map(int, input().split())) for _ in range(n)]
    horizontal_spec = [list(map(int, input().split())) for _ in range(n)]
    return n, vertical_spec, horizontal_spec

def solve(n, vertical_spec, horizontal_spec):
    # Initialize the solution with all borders unmarked
    vertical_sol = ['0' * (n+1)] * (n+1)
    horizontal_sol = ['0' * n] * (n+1)

    # Iterate through the rows and columns of the specification
    for i in range(n):
        for j in range(n):
            # If the current cell is marked with a bar, continue to the next cell
            if vertical_sol[i][j] == '1' or horizontal_sol[i][j] == '1':
                continue

            # Get the vertical and horizontal specifications for the current cell
            vertical_group_size = vertical_spec[i][j]
            horizontal_group_size = horizontal_spec[i][j]

            # If the vertical specification is 0, the current cell cannot be marked with a bar
            if vertical_group_size == 0:
                continue

            # If the horizontal specification is 0, the current cell cannot be marked with a bar
            if horizontal_group_size == 0:
                continue

            # If the current cell is not marked with a bar, try to mark it with a bar
            vertical_sol[i] = vertical_sol[i][:j] + '1' + vertical_sol[i][j+1:]
            horizontal_sol[i] = horizontal_sol[i][:j] + '1' + horizontal_sol[i][j+1:]

            # If the current cell is marked with a bar, update the solution
            vertical_sol[i+1] = vertical_sol[i+1][:j] + '0' + vertical_sol[i+1][j+1:]
            horizontal_sol[i+1] = horizontal_sol[i+1][:j] + '0' + horizontal_sol[i+1][j+1:]

    return vertical_sol, horizontal_sol

def print_output(vertical_sol, horizontal_sol):
    for row in vertical_sol:
        print(row)
    for row in horizontal_sol:
        print(row)

if __name__ == '__main__':
    n, vertical_spec, horizontal_spec = get_input()
    vertical_sol, horizontal_sol = solve(n, vertical_spec, horizontal_spec)
    print_output(vertical_sol, horizontal_sol)

