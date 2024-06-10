
def minimum_books_to_remove(q, queries):
    left_books = []
    right_books = []
    book_positions = {}

    def place_book_left(book_id):
        left_books.insert(0, book_id)
        book_positions[book_id] = 0

    def place_book_right(book_id):
        right_books.append(book_id)
        book_positions[book_id] = len(right_books) - 1

    def calculate_min_books_to_remove(book_id):
        if book_id in book_positions:
            left_index = book_positions.get(book_id)
            right_index = len(right_books) - left_index - 1
            return min(left_index, right_index)
        return 0

    for query in queries:
        query_type, book_id = query.split()
        book_id = int(book_id)
        if query_type == 'L':
            place_book_left(book_id)
        elif query_type == 'R':
            place_book_right(book_id)
        else:
            print(calculate_min_books_to_remove(book_id))

if __name__ == "__main__":
    q = int(input())
    queries = [input().strip() for _ in range(q)]
    minimum_books_to_remove(q, queries)
