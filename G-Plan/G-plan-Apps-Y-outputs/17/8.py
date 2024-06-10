ess_queries(q, queries):
    left_books = []
    right_books = []
    book_positions = {}

    def calculate_min_books_to_remove(book_id):
        left_index = book_positions[book_id] if book_id in book_positions else -1
        right_index = len(left_books) + right_books.index(book_id) if book_id in right_books else -1
        return min(left_index, len(left_books) - left_index - 1, right_index, len(right_books) - right_index - 1)

    for query in queries:
        query_type, book_id = query.split()
        if query_type == 'L':
            left_books.insert(0, book_id)
            book_positions[book_id] = 0
        elif query_type == 'R':
            right_books.append(book_id)
            book_positions[book_id] = len(left_books) + len(right_books) - 1
        else:
            print(calculate_min_books_to_remove(book_id))

if __name__ == "__main__":
    q = int(input())
    queries = [input().strip() for _ in range(q)]
    process_queries(q, queries)
