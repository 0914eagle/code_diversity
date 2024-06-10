
def get_min_moves(a):
    n = len(a)
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the start and end indices of the segment to collect
    start, end = 0, 0
    # Loop through each position on the bookshelf
    for i in range(n):
        # If there is a book at the current position
        if a[i] == 1:
            # If this is the start of a new segment
            if start == 0:
                # Set the start index to the current position
                start = i
            # Set the end index to the current position
            end = i
        # If this is the end of a segment
        if a[i] == 0 and start != 0:
            # Calculate the length of the segment
            length = end - start + 1
            # If the segment is not contiguous
            if length > 1:
                # Calculate the number of moves required to shift the segment to the right
                right_moves = (length - 1) // 2
                # Calculate the number of moves required to shift the segment to the left
                left_moves = length - right_moves - 1
                # Update the number of moves
                moves += min(right_moves, left_moves)
            # Reset the start and end indices
            start, end = 0, 0
    return moves

def solve(a):
    return get_min_moves(a)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

