
def solve(boys, girls, boy_books, girl_books):
    # Initialize variables
    presentations = 0
    books = {}

    # Add books to dictionary
    for i in range(len(boys)):
        books[boys[i]] = boy_books[i]
    for i in range(len(girls)):
        books[girls[i]] = girl_books[i]

    # Sort books by number of books read
    sorted_books = sorted(books.items(), key=lambda x: len(x[1]), reverse=True)

    # Iterate through sorted books and assign presentations
    for student, book_list in sorted_books:
        presentations += 1
        for book in book_list:
            if book in books:
                books[student].remove(book)
                if len(books[student]) == 0:
                    del books[student]

    return presentations

