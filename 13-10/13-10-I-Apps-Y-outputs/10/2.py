
def get_grid_size(grid_string):
    return tuple(map(int, grid_string.split()))

def get_grid_bombs(grid_string):
    return [bomb for bomb in grid_string if bomb == '#']

def get_grid_empty_squares(grid_string):
    return [empty for empty in grid_string if empty == '.']

def get_adjacent_bombs(grid_string, empty_square):
    row, col = empty_square
    adjacent_squares = [(row-1, col-1), (row-1, col), (row-1, col+1),
                        (row, col-1), (row, col+1),
                        (row+1, col-1), (row+1, col), (row+1, col+1)]
    return len([bomb for bomb in grid_string if bomb in adjacent_squares])

def replace_empty_squares(grid_string, empty_squares):
    for empty_square in empty_squares:
        row, col = empty_square
        bombs = get_adjacent_bombs(grid_string, empty_square)
        grid_string = grid_string[:row*col] + str(bombs) + grid_string[row*col+1:]
    return grid_string

def solve(grid_string):
    size = get_grid_size(grid_string)
    bombs = get_grid_bombs(grid_string)
    empty_squares = get_grid_empty_squares(grid_string)
    grid_string = replace_empty_squares(grid_string, empty_squares)
    return grid_string

if __name__ == '__main__':
    grid_string = input()
    print(solve(grid_string))

