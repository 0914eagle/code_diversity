
def get_next_color(current_color):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = alphabet.index(current_color)
    next_index = (index + 1) % len(alphabet)
    return alphabet[next_index]

def get_next_position(current_position, direction):
    rows, cols = current_position
    if direction == 'U':
        return rows - 1, cols
    elif direction == 'D':
        return rows + 1, cols
    elif direction == 'L':
        return rows, cols - 1
    else:
        return rows, cols + 1

def get_zamboni_path(r, c, i, j, n):
    direction = 'U'
    current_color = 'A'
    path = []
    for _ in range(n):
        path.append(current_color)
        current_color = get_next_color(current_color)
        direction = 'R' if direction == 'D' else 'L' if direction == 'U' else direction
        i, j = get_next_position((i, j), direction)
        if i < 0:
            i = r - 1
        elif i == r:
            i = 0
        if j < 0:
            j = c - 1
        elif j == c:
            j = 0
    return ''.join(path)

def main():
    r, c, i, j, n = map(int, input().split())
    print(get_zamboni_path(r, c, i, j, n))

if __name__ == '__main__':
    main()

