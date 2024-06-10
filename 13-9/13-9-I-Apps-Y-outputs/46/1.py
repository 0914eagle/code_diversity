
def get_min_moves(a):
    # Find the first and last positions of books on the shelf
    first_book = next((i for i, x in enumerate(a) if x == 1), None)
    last_book = next(reversed([i for i, x in enumerate(a) if x == 1]), None)

    # Initialize the number of moves to 0
    moves = 0

    # Loop until all books are on the same side of the shelf
    while first_book != last_book:
        # If the first book is on the left side of the shelf, move it to the right
        if first_book < last_book:
            a = a[1:] + [0]
            last_book -= 1
        # If the first book is on the right side of the shelf, move it to the left
        else:
            a = [0] + a[:-1]
            first_book += 1

        # Update the number of moves
        moves += 1

    # Return the minimum number of moves
    return moves

def solve(a):
    # Find the minimum number of moves required to collect all the books on the shelf as a contiguous segment
    min_moves = get_min_moves(a)

    # Return the minimum number of moves
    return min_moves

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input())

    # Loop through each test case
    for _ in range(t):
        # Read the number of places on the bookshelf and the positions of the books
        n = int(input())
        a = list(map(int, input().split()))

        # Solve the test case and print the minimum number of moves
        print(solve(a))

