
def f1(board, program):
    # Initialize the turtle's position and direction
    x, y = 0, 0
    direction = 'R'

    # Iterate through the program
    for instruction in program:
        # Move the turtle forward
        if instruction == 'F':
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1

        # Turn the turtle right
        elif instruction == 'R':
            direction = 'R'

        # Turn the turtle left
        elif instruction == 'L':
            direction = 'L'

        # Fire the laser
        elif instruction == 'X':
            if board[y][x] == 'I':
                board[y][x] = '.'
            else:
                return 'Bug!'

    # Check if the turtle is on the diamond
    if board[y][x] == 'D':
        return 'Diamond!'
    else:
        return 'Bug!'

def f2(board, program):
    # Initialize the turtle's position and direction
    x, y = 0, 0
    direction = 'R'

    # Iterate through the program
    for instruction in program:
        # Move the turtle forward
        if instruction == 'F':
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1

        # Turn the turtle right
        elif instruction == 'R':
            direction = 'R'

        # Turn the turtle left
        elif instruction == 'L':
            direction = 'L'

        # Fire the laser
        elif instruction == 'X':
            if board[y][x] == 'I':
                board[y][x] = '.'
            else:
                return 'Bug!'

    # Check if the turtle is on the diamond
    if board[y][x] == 'D':
        return 'Diamond!'
    else:
        return 'Bug!'

if __name__ == '__main__':
    board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
    ]
    program = 'FLFRXFLFRFLFRF'
    print(f1(board, program))
    print(f2(board, program))

