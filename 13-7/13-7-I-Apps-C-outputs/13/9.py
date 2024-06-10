
import math

def get_next_color(current_color):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    current_index = alphabet.index(current_color)
    next_index = (current_index + 1) % len(alphabet)
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

def get_final_position(rows, cols, num_steps):
    current_position = (1, 1)
    current_direction = 'U'
    current_color = 'A'
    for _ in range(num_steps):
        next_position = get_next_position(current_position, current_direction)
        if next_position[0] < 1 or next_position[0] > rows or next_position[1] < 1 or next_position[1] > cols:
            next_position = (next_position[0] - 1, next_position[1] - 1)
        current_position = next_position
        current_direction = chr((ord(current_direction) + 1) % 4)
        current_color = get_next_color(current_color)
    return current_position, current_color

def get_ice_rink(rows, cols, num_steps):
    ice_rink = [['.'] * cols for _ in range(rows)]
    final_position, final_color = get_final_position(rows, cols, num_steps)
    ice_rink[final_position[0] - 1][final_position[1] - 1] = '@'
    return ice_rink

def main():
    rows, cols, start_row, start_col, num_steps = map(int, input().split())
    ice_rink = get_ice_rink(rows, cols, num_steps)
    for row in ice_rink:
        print(''.join(row))

if __name__ == '__main__':
    main()

