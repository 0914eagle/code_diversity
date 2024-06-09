
def black_vienna(investigations):
    num_investigations = int(investigations[0])
    investigations = investigations[1:]

    # Initialize a dictionary to store the number of investigations for each suspect
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

    # Initialize a set to store the admissible solutions
    solutions = set()

    # Iterate through the suspect counts and add admissible solutions to the set
    for suspect, count in suspect_counts.items():
        if count == 0:
            solutions.add(suspect)

    return len(solutions)

