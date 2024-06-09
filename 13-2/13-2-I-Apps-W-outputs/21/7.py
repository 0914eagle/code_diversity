
def get_affected_settlements(n, m, d, paths, affected_settlements):
    # Initialize a set to store the affected settlements
    affected_settlements = set(affected_settlements)

    # Iterate over the paths
    for path in paths:
        # Get the ends of the path
        a, b = path

        # Check if the path connects two affected settlements
        if a in affected_settlements and b in affected_settlements:
            # If the path connects two affected settlements, add the other end of the path to the affected settlements set
            affected_settlements.add(a if a != b else b)

    # Return the affected settlements
    return affected_settlements

def get_book_settlements(n, m, d, paths, affected_settlements):
    # Get the affected settlements
    affected_settlements = get_affected_settlements(n, m, d, paths, affected_settlements)

    # Initialize a set to store the book settlements
    book_settlements = set()

    # Iterate over the affected settlements
    for settlement in affected_settlements:
        # Check if the settlement is within the damage range of the Book of Evil
        if settlement in range(max(0, d + 1), n):
            # If the settlement is within the damage range, add it to the book settlements set
            book_settlements.add(settlement)

    # Return the book settlements
    return book_settlements

def main():
    # Read the input
    n, m, d = map(int, input().split())
    paths = [tuple(map(int, input().split())) for _ in range(n - 1)]
    affected_settlements = list(map(int, input().split()))

    # Get the book settlements
    book_settlements = get_book_settlements(n, m, d, paths, affected_settlements)

    # Print the number of book settlements
    print(len(book_settlements))

if __name__ == '__main__':
    main()

