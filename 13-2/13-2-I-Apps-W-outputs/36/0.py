
def solve(n, m, k, books):
    # Sort the books by their reading time in ascending order
    books = sorted(books, key=lambda x: x[0])

    # Initialize the minimum total reading time and the chosen books
    min_time = float('inf')
    chosen_books = []

    # Iterate over all possible combinations of books
    for b in range(1, 2 ** n):
        # Convert the binary representation of b to a list of indices of chosen books
        books_chosen = [i for i in range(n) if b & (1 << i)]

        # Check if the number of chosen books is less than or equal to m
        if len(books_chosen) <= m:
            # Calculate the total reading time of the chosen books
            time = sum(books[i][0] for i in books_chosen)

            # Check if the total reading time is less than or equal to the minimum total reading time
            if time <= min_time:
                # Check if the number of liked books by Alice and Bob is greater than or equal to k
                if all(books[i][1] + books[i][2] >= k for i in books_chosen):
                    # Update the minimum total reading time and the chosen books
                    min_time = time
                    chosen_books = books_chosen

    # Check if a solution exists
    if not chosen_books:
        return [-1]

    # Return the minimum total reading time and the chosen books
    return [min_time] + chosen_books

