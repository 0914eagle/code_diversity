
def get_smallest_t(n, crush):
    # Initialize a dictionary to store the number of rounds required for each person to become the Joon-Joon
    rounds_required = {i: 0 for i in range(1, n + 1)}

    # Loop through each person and their crush
    for i in range(1, n + 1):
        current_person = i
        current_rounds = 0
        while current_person != i:
            current_rounds += 1
            current_person = crush[current_person - 1]
        rounds_required[i] = current_rounds

    # Find the smallest value of t that satisfies the condition for all people
    t = min(rounds_required.values())

    # Check if t satisfies the condition for all people
    if all(rounds_required[i] >= t for i in range(1, n + 1)):
        return t
    else:
        return -1

