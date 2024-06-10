
def calculate_min_books(q, queries):
    left_books = []
    right_books = []
    book_positions = {}

    def place_book_left(book_id):
        left_books.insert(0, book_id)
        book_positions[book_id] = 0

    def place_book_right(book_id):
        right_books.append(book_id)
        book_positions[book_id] = len(right_books) - 1

    def query_min_books(book_id):
        if book_id in book_positions:
            book_pos = book_positions[book_id]
            return min(book_pos, len(right_books) - book_pos - 1)
        return 0

    results = []
    for query in queries:
        query_type, book_id = query.split()
        if query_type == 'L':
            place_book_left(int(book_id))
        elif query_type == 'R':
            place_book_right(int(book_id))
        else:
            results.append(query_min_books(int(book_id)))

    return results

if __name__ == "__main__":
    q = int(input())
    queries = [input().strip() for _ in range(q)]
    results = calculate_min_books(q, queries)
    for result in results:
        print(result)
