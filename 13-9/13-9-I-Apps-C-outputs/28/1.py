
def find_largest_square_killer(memory):
    rows, cols = len(memory), len(memory[0])
    largest_killer = 0

    for row in range(rows):
        for col in range(cols):
            if memory[row][col] == "1":
                current_killer = 1
                for r in range(row, rows):
                    for c in range(col, cols):
                        if memory[r][c] == "1":
                            current_killer += 1
                        else:
                            break
                    if current_killer > largest_killer:
                        largest_killer = current_killer
                    current_killer = 1
                    for r in range(row, -1, -1):
                        for c in range(col, -1, -1):
                            if memory[r][c] == "1":
                                current_killer += 1
                            else:
                                break
                        if current_killer > largest_killer:
                            largest_killer = current_killer
                        current_killer = 1

    return largest_killer

