
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
                # If the book with the given index is to the left of the leftmost book, pop books from the left until the leftmost book is the book with the given index
                if index < shelf.index(shelf[0]):
                    print(shelf.index(shelf[0]) - index)
                # If the book with the given index is to the right of the rightmost book, pop books from the right until the rightmost book is the book with the given index
                else:
                    print(index - shelf.index(shelf[-1]))
    return shelf

