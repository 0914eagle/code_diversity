
def f1(n, m, field):
    # Initialize variables
    moves = 0
    dwarves = []
    candy = []

    # Parse the field
    for i in range(n):
        for j in range(m):
            if field[i][j] == "G":
                dwarves.append((i, j))
            elif field[i][j] == "S":
                candy.append((i, j))

    # Game loop
    while dwarves and candy:
        # Find the closest dwarf to the candy
        min_dist = float("inf")
        for dwarf in dwarves:
            for candy_pos in candy:
                dist = abs(dwarf[0] - candy_pos[0]) + abs(dwarf[1] - candy_pos[1])
                if dist < min_dist:
                    min_dist = dist
                    closest_dwarf = dwarf
                    closest_candy = candy_pos

        # Move the closest dwarf to the candy
        dwarves.remove(closest_dwarf)
        candy.remove(closest_candy)
        moves += 1

    # Check if all dwarves are at the candy
    if not dwarves:
        return moves
    else:
        return -1

def f2(n, m, field):
    # Initialize variables
    moves = 0
    dwarves = []
    candy = []

    # Parse the field
    for i in range(n):
        for j in range(m):
            if field[i][j] == "G":
                dwarves.append((i, j))
            elif field[i][j] == "S":
                candy.append((i, j))

    # Game loop
    while dwarves and candy:
        # Find the closest dwarf to the candy
        min_dist = float("inf")
        for dwarf in dwarves:
            for candy_pos in candy:
                dist = abs(dwarf[0] - candy_pos[0]) + abs(dwarf[1] - candy_pos[1])
                if dist < min_dist:
                    min_dist = dist
                    closest_dwarf = dwarf
                    closest_candy = candy_pos

        # Move the closest dwarf to the candy
        dwarves.remove(closest_dwarf)
        candy.remove(closest_candy)
        moves += 1

        # Check if all dwarves are at the candy
        if not dwarves:
            return moves

    # If the game is not solvable, return -1
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    field = []
    for _ in range(n):
        field.append(input())
    print(f2(n, m, field))

