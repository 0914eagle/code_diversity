
def get_next_color(current_color):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    current_index = alphabet.index(current_color)
    next_index = (current_index + 1) % len(alphabet)
    return alphabet[next_index]

def get_next_location(current_location, direction, size):
    row, col = current_location
    if direction == 'up':
        return row - size, col
    elif direction == 'down':
        return row + size, col
    elif direction == 'left':
        return row, col - size
    else:
        return row, col + size

def get_ice_color(current_location, grid):
    row, col = current_location
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return '.'
    return grid[row][col]

def clean_ice(grid, size):
    current_location = (0, 0)
    current_color = 'A'
    direction = 'up'
    step_size = 1
    for _ in range(size):
        next_location = get_next_location(current_location, direction, step_size)
        next_color = get_next_color(current_color)
        grid[next_location[0]][next_location[1]] = next_color
        current_location = next_location
        current_color = next_color
        step_size += 1
        direction = 'right' if direction == 'up' else 'down' if direction == 'left' else 'left'
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def main():
    r, c, i, j, n = map(int, input().split())
    grid = [['.'] * c for _ in range(r)]
    clean_ice(grid, n)
    print_grid(grid)

if __name__ == '__main__':
    main()

