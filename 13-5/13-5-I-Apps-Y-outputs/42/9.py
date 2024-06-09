
def solve(n, q, p, queries):
    # Initialize a list to store the command spreading sequence
    sequence = []

    # Loop through each query
    for query in queries:
        # Get the current officer and the required position in the sequence
        current_officer, required_position = query

        # Initialize a set to keep track of the officers who have received the command
        received_officers = set()

        # Initialize a queue to store the officers who still need to receive the command
        queue = [current_officer]

        # Loop until the queue is empty
        while queue:
            # Get the current officer from the queue
            current_officer = queue.pop(0)

            # If the current officer has not received the command yet, add them to the sequence and mark them as received
            if current_officer not in received_officers:
                sequence.append(current_officer)
                received_officers.add(current_officer)

            # Add the current officer's direct subordinates to the queue
            for subordinate in range(current_officer + 1, n + 1):
                if p[subordinate - 1] == current_officer:
                    queue.append(subordinate)

        # If the required position is beyond the length of the sequence, return -1
        if required_position > len(sequence):
            return -1

        # Return the officer at the required position in the sequence
        return sequence[required_position - 1]

# Test case 1
n = 9
q = 6
p = [1, 1, 1, 3, 5, 3, 5, 7]
queries = [(3, 1), (1, 5), (3, 4), (7, 3), (1, 8), (1, 9)]
print(solve(n, q, p, queries))

# Test case 2
n = 10
q = 4
p = [1, 1, 1, 3, 5, 3, 5, 7, 9, 2]
queries = [(3, 1), (1, 5), (7, 4), (1, 10)]
print(solve(n, q, p, queries))

# Test case 3
n = 15
q = 7
p = [1, 1, 1, 3, 5, 3, 5, 7, 9, 2, 4, 6, 10, 12, 14]
queries = [(3, 1), (1, 5), (7, 4), (1, 10), (14, 2), (10, 6), (5, 3)]
print(solve(n, q, p, queries))

