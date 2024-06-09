
def black_vienna(investigations):
    num_investigations = int(investigations[0])
    investigations = investigations[1:]

    # Initialize a dictionary to store the number of times each suspect is mentioned in the investigations
    suspect_counts = {}
    for i in range(1, 27):
        suspect_counts[chr(i + 64)] = 0

    # Iterate through the investigations and update the suspect counts
    for investigation in investigations:
        suspects, player, reply = investigation.split()
        suspect1, suspect2 = suspects
        if player == "1":
            suspect_counts[suspect1] += 1
            suspect_counts[suspect2] += 1
        else:
            suspect_counts[suspect1] -= 1
            suspect_counts[suspect2] -= 1

    # Initialize a list to store the admissible solutions
    solutions = []

    # Iterate through the suspect counts and check if each suspect is in the Black Vienna circle
    for suspect, count in suspect_counts.items():
        if count == 0:
            solutions.append(suspect)

    # Return the number of admissible solutions
    return len(solutions)

