
def solve(boys, girls, boys_books, girls_books):
    # Initialize variables
    presentations = 0
    books = {}

    # Add books from boys
    for i in range(len(boys)):
        for book in boys_books[i]:
            if book not in books:
                books[book] = 1
            else:
                books[book] += 1

    # Add books from girls
    for i in range(len(girls)):
        for book in girls_books[i]:
            if book not in books:
                books[book] = 1
            else:
                books[book] += 1

    # Calculate the minimum number of presentations needed
    for book, count in books.items():
        presentations += count // 2 + count % 2

    return presentations

