
def solve(n, q, p, queries):
    # Initialize a list to store the command spreading sequence
    sequence = []

    # Iterate over each query
    for query in queries:
        # Initialize a set to store the indices of the officers who have received the command
        received = set()

        # Initialize the current officer as the query officer
        current = query[0]

        # Iterate until the command is spread to all officers
        while len(sequence) < n:
            # If the current officer has not received the command yet, add them to the sequence
            if current not in received:
                sequence.append(current)
                received.add(current)

            # Find the next direct subordinate of the current officer who has not received the command yet
            next_subordinate = None
            for subordinate in range(current + 1, n + 1):
                if subordinate not in received and p[subordinate - 1] == current:
                    next_subordinate = subordinate
                    break

            # If there is no next direct subordinate, break the loop
            if next_subordinate is None:
                break

            # Set the current officer as the next direct subordinate
            current = next_subordinate

        # If the command has been spread to all officers, return the k-th element of the sequence
        if len(sequence) == n:
            return sequence[query[1] - 1]

    # If the command has not been spread to all officers, return -1
    return -1

