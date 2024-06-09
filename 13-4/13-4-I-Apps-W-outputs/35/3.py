
def is_valid_cell(row, col, n):
    if row < 1 or row > n or col < 1 or col > 2:
        return False
    return True

def get_neighboring_cells(row, col, n):
    neighboring_cells = []
    if row > 1:
        neighboring_cells.append((row - 1, col))
    if row < n:
        neighboring_cells.append((row + 1, col))
    if col == 1:
        neighboring_cells.append((row, 2))
    if col == 2:
        neighboring_cells.append((row, 1))
    return neighboring_cells

def get_valid_cells(n, reclaimed_cells):
    valid_cells = []
    for row in range(1, n + 1):
        for col in range(1, 3):
            if (row, col) not in reclaimed_cells and is_valid_cell(row, col, n):
                valid_cells.append((row, col))
    return valid_cells

def get_winner(n, reclaimed_cells):
    valid_cells = get_valid_cells(n, reclaimed_cells)
    if len(valid_cells) == 0:
        return "LOSE"
    else:
        return "WIN"

def main():
    n, m = map(int, input().split())
    reclaimed_cells = []
    for _ in range(m):
        row, col = map(int, input().split())
        reclaimed_cells.append((row, col))
    print(get_winner(n, reclaimed_cells))

if __name__ == '__main__':
    main()

