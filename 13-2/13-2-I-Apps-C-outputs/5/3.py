
def f1(n, r, m):
    # Initialize variables
    tricks = []
    total_time = 0
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
        total_time += t
        expected_time += p * (total_time - t) + (1 - p) * (total_time + d)

    # Calculate expected time to set a new record
    expected_time = expected_time / (1 - (1 - p) ** m)

    return expected_time

