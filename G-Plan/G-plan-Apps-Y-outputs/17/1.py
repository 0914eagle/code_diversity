
def minimum_books_to_remove(q, queries):
    left_books = []
    right_books = []
    book_positions = {}

    def update_book_positions(book_id):
        book_positions[book_id] = len(left_books) + 1

    def calculate_books_to_remove(book_id):
        if book_id in book_positions:
            book_index = book_positions[book_id]
            return min(book_index - 1, len(left_books) - book_index, len(right_books) - book_index)
        return 0

    for query in queries:
        query_type, book_id = query.split()
        if query_type == 'L':
            left_books.insert(0, book_id)
            update_book_positions(book_id)
        elif query_type == 'R':
            right_books.append(book_id)
            update_book_positions(book_id)
        else:
            print(calculate_books_to_remove(book_id))

if __name__ == "__main__":
    q = int(input())
    queries = [input().strip() for _ in range(q)]
    minimum_books_to_remove(q, queries)
