
import sys

def get_next_color(current_color):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(current_color)
    return alphabet[(index + 1) % len(alphabet)]

def get_next_position(position, direction):
    row, col = position
    if direction == "UP":
        return row - 1, col
    elif direction == "DOWN":
        return row + 1, col
    elif direction == "LEFT":
        return row, col - 1
    else:
        return row, col + 1

def get_next_direction(direction):
    if direction == "UP":
        return "LEFT"
    elif direction == "DOWN":
        return "RIGHT"
    elif direction == "LEFT":
        return "DOWN"
    else:
        return "UP"

def get_color(position, r, c):
    row, col = position
    if row < 0 or row >= r or col < 0 or col >= c:
        return "."
    else:
        return "A"

def get_final_position(r, c, i, j, n):
    direction = "UP"
    position = (i, j)
    step_size = 1
    for _ in range(n):
        color = get_color(position, r, c)
        next_position = get_next_position(position, direction)
        next_direction = get_next_direction(direction)
        step_size += 1
        position = next_position
        direction = next_direction
    return position

def solve(r, c, i, j, n):
    final_position = get_final_position(r, c, i, j, n)
    row, col = final_position
    return [["." for _ in range(c)] for _ in range(r)]

def main():
    r, c, i, j, n = map(int, sys.stdin.readline().split())
    result = solve(r, c, i, j, n)
    for row in result:
        print("".join(row))

if __name__ == '__main__':
    main()

