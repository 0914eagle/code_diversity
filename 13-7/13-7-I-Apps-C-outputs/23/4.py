
def is_possible(initial_board, target_board):
    # Initialize a queue to store the blocks to be processed
    queue = [(0, 0)]

    # Initialize a set to keep track of the blocks that have been processed
    processed = set()

    # Loop until the queue is empty
    while queue:
        # Dequeue a block from the queue
        row, col = queue.pop(0)

        # If the block is in the target board, mark it as processed and add its neighbors to the queue
        if target_board[row][col] == "X":
            processed.add((row, col))
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r < len(initial_board) and 0 <= c < len(initial_board[0]) and (r, c) not in processed and initial_board[r][c] == "X":
                    queue.append((r, c))

    # If all the blocks in the target board have been processed, return True, otherwise return False
    return len(processed) == len(target_board)

def get_moves(initial_board, target_board):
    # Initialize a list to store the moves
    moves = []

    # Loop through the rows of the initial board
    for row in range(len(initial_board)):
        # Loop through the columns of the initial board
        for col in range(len(initial_board[0])):
            # If the current block is not in the target board, skip it
            if target_board[row][col] != "X":
                continue

            # If the current block is in the target board, check if it can be reached from the initial board
            if can_reach_block(initial_board, target_board, row, col):
                # If it can be reached, add the move to the list of moves
                moves.append((row, col))

    # Return the list of moves
    return moves

def can_reach_block(initial_board, target_board, row, col):
    # If the current block is already in the initial board, return True
    if initial_board[row][col] == "X":
        return True

    # If the current block is not in the initial board, check if it can be reached from any of its neighbors
    for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        # If the neighboring block is in the initial board and can be reached from it, return True
        if 0 <= r < len(initial_board) and 0 <= c < len(initial_board[0]) and initial_board[r][c] == "X" and can_reach_block(initial_board, target_board, r, c):
            return True

    # If none of the neighboring blocks can be reached, return False
    return False

if __name__ == '__main__':
    # Read the input
    N, M, B = map(int, input().split())
    target_board = [input() for _ in range(N)]

    # Initialize the initial board with a single block
    initial_board = [["."] * M for _ in range(N)]
    initial_board[0][0] = "X"

    # Check if the target board can be reached from the initial board
    if is_possible(initial_board, target_board):
        # If it can be reached, get the list of moves to reach the target board
        moves = get_moves(initial_board, target_board)

        # Print the list of moves
        print("possible")
        for move in moves:
            print(move[0], move[1])
    else:
        # If it cannot be reached, print "impossible"
        print("impossible")

