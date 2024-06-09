
def get_input():
    R, S = map(int, input().split())
    seating_order = []
    for _ in range(R):
        seating_order.append(list(input()))
    return R, S, seating_order

def get_neighbors(row, col, seating_order):
    neighbors = []
    if row > 0 and col > 0 and seating_order[row-1][col-1] == 'o':
        neighbors.append((row-1, col-1))
    if row > 0 and seating_order[row-1][col] == 'o':
        neighbors.append((row-1, col))
    if row > 0 and col < S-1 and seating_order[row-1][col+1] == 'o':
        neighbors.append((row-1, col+1))
    if col > 0 and seating_order[row][col-1] == 'o':
        neighbors.append((row, col-1))
    if col < S-1 and seating_order[row][col+1] == 'o':
        neighbors.append((row, col+1))
    if row < R-1 and col > 0 and seating_order[row+1][col-1] == 'o':
        neighbors.append((row+1, col-1))
    if row < R-1 and seating_order[row+1][col] == 'o':
        neighbors.append((row+1, col))
    if row < R-1 and col < S-1 and seating_order[row+1][col+1] == 'o':
        neighbors.append((row+1, col+1))
    return neighbors

def get_handshakes(seating_order):
    handshakes = 0
    for row in range(len(seating_order)):
        for col in range(len(seating_order[row])):
            if seating_order[row][col] == 'o':
                neighbors = get_neighbors(row, col, seating_order)
                handshakes += len(neighbors)
    return handshakes

def main():
    R, S, seating_order = get_input()
    handshakes = get_handshakes(seating_order)
    print(handshakes)

if __name__ == '__main__':
    main()

