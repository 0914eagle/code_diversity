
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

            # Add the current officer to the set of received officers
            received_officers.add(current_officer)

            # Add the direct subordinates of the current officer to the queue
            for subordinate in range(current_officer + 1, n + 1):
                if p[subordinate - 1] == current_officer:
                    queue.append(subordinate)

        # If the required position is less than or equal to the number of received officers, return the officer at that position
        if required_position <= len(received_officers):
            return list(received_officers)[required_position - 1]
        # Otherwise, return -1
        else:
            return -1

    return sequence

