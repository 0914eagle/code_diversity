
def solve(n, q, p, queries):
    # Initialize a list to store the command spreading sequence
    sequence = []

    # Iterate over each query
    for query in queries:
        # Initialize a set to store the officers who have received the command
        received = set()

        # Initialize the current officer as the query officer
        current = query[0]

        # Iterate until the command has been spread to all subordinates
        while current not in received:
            # Add the current officer to the set of received officers
            received.add(current)

            # If the current officer has any direct subordinates, choose the one with the minimum index
            if current in p and p[current] not in received:
                current = p[current]
            # Otherwise, the command has been spread to all subordinates, so break the loop
            else:
                break

        # Add the current officer to the command spreading sequence
        sequence.append(current)

    # Return the k-th element of the command spreading sequence for the i-th query
    return sequence[query[1] - 1] if query[1] <= len(sequence) else -1

