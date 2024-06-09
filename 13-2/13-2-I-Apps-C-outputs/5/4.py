
def f1(n, r, m):
    # Initialize variables
    tricks = []
    expected_time = 0

    # Read input data
    for i in range(m):
        t, p, d = map(int, input().split())
        tricks.append((t, p, d))

    # Sort tricks by time
    tricks.sort(key=lambda x: x[0])

    # Loop through tricks and calculate expected time
    for i in range(m):
        t, p, d = tricks[i]
        expected_time += t * p + d * (1 - p)

    # Add time for rest of route
    expected_time += n - tricks[-1][0]

    return expected_time

