
def solve(queries):
    # Initialize the shelf with a single book
    shelf = [1]
    
    # Iterate over the queries
    for query in queries:
        # If the query is of type L, add the book to the left of the leftmost existing book
        if query[0] == "L":
            shelf.insert(0, query[1])
        # If the query is of type R, add the book to the right of the rightmost existing book
        elif query[0] == "R":
            shelf.append(query[1])
        # If the query is of type ?, find the minimum number of books to pop from the left or from the right
        elif query[0] == "?":
            # If the book with the given index is already the leftmost or rightmost book, return 0
            if query[1] == shelf[0] or query[1] == shelf[-1]:
                print(0)
            # Otherwise, find the index of the book with the given index
            else:
                index = shelf.index(query[1])
                # If the book is in the left half of the shelf, pop books from the left until the book with the given index is the leftmost book
                if index <= len(shelf) // 2:
                    print(len(shelf) - index)
                # If the book is in the right half of the shelf, pop books from the right until the book with the given index is the rightmost book
                else:
                    print(index + 1)

# Test the function with the sample input
queries = [
    ["L", 1],
    ["R", 2],
    ["R", 3],
    ["?", 2],
    ["L", 4],
    ["?", 1],
    ["L", 5],
    ["?", 1]
]
solve(queries)

