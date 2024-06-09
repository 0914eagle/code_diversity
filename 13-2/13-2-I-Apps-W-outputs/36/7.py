
def solve(n, m, k, books):
    # Sort the books by their reading time in ascending order
    books = sorted(books, key=lambda x: x[0])

    # Initialize the minimum total reading time and the chosen books
    min_time = float('inf')
    chosen_books = []

    # Iterate over all possible combinations of books
    for b in itertools.combinations(books, m):
        # Check if the combination of books satisfies the conditions
        if sum(b[i][1] for i in range(m)) >= k and sum(b[i][2] for i in range(m)) >= k:
            # Calculate the total reading time of the current combination
            time = sum(b[i][0] for i in range(m))

            # Check if the current combination is the optimal one
            if time < min_time:
                min_time = time
                chosen_books = b

    # If no suitable combination of books was found, return -1
    if not chosen_books:
        return -1

    # Otherwise, return the minimum total reading time and the indices of the chosen books
    return min_time, [i + 1 for i in range(m) if chosen_books[i]]

