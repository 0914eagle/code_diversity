
def f1(n, m):
    # Initialize the game field
    game_field = []
    for _ in range(n):
        game_field.append(input())

    # Initialize the number of moves
    moves = 0

    # Loop through each line of the game field
    for i in range(n):
        # Check if the line contains a dwarf and a candy
        if "G" in game_field[i] and "S" in game_field[i]:
            # Find the index of the dwarf and the candy
            dwarf_index = game_field[i].index("G")
            candy_index = game_field[i].index("S")

            # Calculate the number of moves needed to move the dwarf to the candy
            moves += abs(dwarf_index - candy_index)

            # Move the dwarf to the candy
            game_field[i] = game_field[i][:dwarf_index] + "G" + game_field[i][dwarf_index + 1:]

    # Return the minimum number of moves
    return moves

def f2(n, m):
    # Initialize the game field
    game_field = []
    for _ in range(n):
        game_field.append(input())

    # Initialize the number of moves
    moves = 0

    # Loop through each line of the game field
    for i in range(n):
        # Check if the line contains a dwarf and a candy
        if "G" in game_field[i] and "S" in game_field[i]:
            # Find the index of the dwarf and the candy
            dwarf_index = game_field[i].index("G")
            candy_index = game_field[i].index("S")

            # Calculate the number of moves needed to move the dwarf to the candy
            moves += abs(dwarf_index - candy_index)

            # Move the dwarf to the candy
            game_field[i] = game_field[i][:dwarf_index] + "G" + game_field[i][dwarf_index + 1:]

    # Return the minimum number of moves
    return moves

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

