
def find_first_return_day(n, p):
    # Initialize a dictionary to store the day number for each kid
    days = {i: 1 for i in range(1, n + 1)}
    # Loop through each day
    for day in range(2, n + 1):
        # Loop through each kid
        for i in range(1, n + 1):
            # Find the kid that will receive the book
            receiver = p[i - 1]
            # If the receiver is not the current kid, update the day number
            if receiver != i:
                days[i] = day
                break
    return days

def solve(queries):
    for query in queries:
        n, p = query
        print(*find_first_return_day(n, p))

if __name__ == '__main__':
    solve([(5, [1, 2, 3, 4, 5]), (3, [2, 3, 1]), (6, [4, 6, 2, 1, 5, 3]), (1, [1]), (4, [3, 4, 1, 2]), (5, [5, 1, 2, 4, 3])])

