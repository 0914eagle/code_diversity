
def get_next_color(current_color):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    current_index = alphabet.index(current_color)
    next_index = (current_index + 1) % len(alphabet)
    return alphabet[next_index]

def get_new_position(position, direction, size):
    row, col = position
    if direction == 'up':
        return (row - 1) % size, col
    elif direction == 'down':
        return (row + 1) % size, col
    elif direction == 'left':
        return row, (col - 1) % size
    else:
        return row, (col + 1) % size

def get_zamboni_path(r, c, i, j, n):
    current_color = 'A'
    current_position = (i, j)
    direction = 'up'
    step_size = 1
    path = ['.' for _ in range(r * c)]
    for _ in range(n):
        for _ in range(step_size):
            current_position = get_new_position(current_position, direction, r)
            path[current_position[0] * c + current_position[1]] = current_color
        current_color = get_next_color(current_color)
        step_size += 1
        direction = 'right' if direction == 'up' else 'left' if direction == 'down' else 'up' if direction == 'left' else 'down'
    return ''.join(path)

def main():
    r, c, i, j, n = map(int, input().split())
    print(get_zamboni_path(r, c, i, j, n))

if __name__ == '__main__':
    main()

