
def solve(n, q, p, queries):
    # Initialize a dictionary to store the subordinates of each officer
    subordinates = {}

    # Iterate over the queries
    for query in queries:
        # Initialize a list to store the sequence of officers who receive the command
        sequence = []

        # Set the current officer as the query officer
        current_officer = query[0]

        # While the current officer has subordinates
        while current_officer in subordinates:
            # Add the current officer to the sequence
            sequence.append(current_officer)

            # Set the current officer as the first subordinate
            current_officer = subordinates[current_officer][0]

        # Add the current officer to the sequence
        sequence.append(current_officer)

        # Print the k-th element of the sequence or -1 if there are fewer than k elements
        print(sequence[query[1] - 1] if query[1] <= len(sequence) else -1)

    return


n = 9
q = 6
p = [1, 1, 1, 3, 5, 3, 5, 7]
queries = [(3, 1), (1, 5), (3, 4), (7, 3), (1, 8), (1, 9)]
solve(n, q, p, queries)

