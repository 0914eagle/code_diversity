
def calculate_min_books(q, queries):
    left_books = []
    right_books = []
    book_positions = {}

    def update_positions(book_id):
        book_positions[book_id] = len(left_books) + 1

    def calculate_min_books_to_remove(book_id):
        book_pos = book_positions[book_id]
        return min(book_pos - 1, len(left_books) - book_pos, len(right_books) - book_pos)

    for query in queries:
        query_type, book_id = query.split()
        book_id = int(book_id)

        if query_type == 'L':
            left_books.insert(0, book_id)
            update_positions(book_id)
        elif query_type == 'R':
            right_books.append(book_id)
            update_positions(book_id)
        elif query_type == '?':
            min_books = calculate_min_books_to_remove(book_id)
            print(min_books)

if __name__ == '__main__':
    q = int(input())
    queries = [input().strip() for _ in range(q)]
    calculate_min_books(q, queries)
