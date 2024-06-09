
def solve(books):
    # Initialize variables
    boys = []
    girls = []
    book_titles = []

    # Split the input into boys, girls, and book titles
    for book in books:
        if book[0].isalpha():
            if book[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                boys.append(book)
            else:
                girls.append(book)
        else:
            book_titles.append(book)

    # Create a dictionary to store the number of books read by each student
    books_read = {}
    for boy in boys:
        books_read[boy] = 0
    for girl in girls:
        books_read[girl] = 0

    # Count the number of books read by each student
    for book in book_titles:
        for boy in boys:
            if boy in book:
                books_read[boy] += 1
        for girl in girls:
            if girl in book:
                books_read[girl] += 1

    # Sort the students by the number of books they have read, in descending order
    sorted_students = sorted(books_read.items(), key=lambda x: x[1], reverse=True)

    # Initialize the minimum number of presentations needed
    presentations_needed = 0

    # Loop through the students and add their books to the presentation
    for student, num_books in sorted_students:
        presentations_needed += 1
        for _ in range(num_books):
            book_titles.remove(student)
        if not book_titles:
            break

    return presentations_needed

