
def solve(bookshelf):
    n = len(bookshelf)
    # Initialize the minimum number of moves to collect all books as infinity
    min_moves = float('inf')
    # Loop through each position on the bookshelf
    for i in range(n):
        # If there is a book at the current position, try to move it to the left and right and check if it forms a contiguous segment
        if bookshelf[i] == 1:
            # Move the book to the left and check if it forms a contiguous segment
            bookshelf[i-1], bookshelf[i] = bookshelf[i], bookshelf[i-1]
            if is_contiguous(bookshelf):
                min_moves = min(min_moves, 1)
            # Move the book to the right and check if it forms a contiguous segment
            bookshelf[i], bookshelf[i+1] = bookshelf[i+1], bookshelf[i]
            if is_contiguous(bookshelf):
                min_moves = min(min_moves, 1)
    return min_moves

def is_contiguous(bookshelf):
    n = len(bookshelf)
    # Loop through each position on the bookshelf
    for i in range(n):
        # If there is no book at the current position, return False
        if bookshelf[i] == 0:
            return False
        # If the current position is not equal to the previous position plus 1, return False
        if i > 0 and bookshelf[i] != bookshelf[i-1] + 1:
            return False
    # If all books are contiguous, return True
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        bookshelf = list(map(int, input().split()))
        print(solve(bookshelf))

