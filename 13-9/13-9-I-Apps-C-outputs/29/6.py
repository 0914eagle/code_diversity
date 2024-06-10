
def get_distances(board, player):
    
    # Initialize the dictionary with the positions of all pieces of the given player
    distances = {pos: 0 for pos in board.keys() if board[pos] == player}
    
    # Loop through all positions in the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # If the current position is empty, skip it
            if board[i][j] == '.':
                continue
            
            # If the current position is not empty and belongs to the given player, calculate the distances to all other pieces of the same player
            pos = (i, j)
            for other_pos in distances.keys():
                # If the current position is not the same as the other position, calculate the distance between them
                if pos != other_pos:
                    distances[pos] = min(distances[pos], abs(i - other_pos[0]) + abs(j - other_pos[1]))
    
    return distances

def get_spread(board, player):
    
    # Get the distances between all pairs of pieces of the given player
    distances = get_distances(board, player)
    
    # Calculate the spread as the sum of the distances
    spread = sum(distances.values())
    
    return spread

def main():
    # Read the input board and player
    rows, cols = map(int, input().split())
    board = {}
    for i in range(rows):
        line = input()
        for j in range(cols):
            board[(i, j)] = line[j]
    
    # Calculate the spreads of both players and print the output
    mirko_spread = get_spread(board, 'M')
    slavko_spread = get_spread(board, 'S')
    print(mirko_spread, slavko_spread)

if __name__ == '__main__':
    main()

