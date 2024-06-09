
def black_vienna(investigations):
    num_investigations = len(investigations)
    num_suspects = 26
    num_circle = 3
    num_solutions = 0

    for i in range(num_investigations):
        suspects = investigations[i][:2]
        player = investigations[i][2]
        reply = investigations[i][3]

        # Initialize a dictionary to store the number of each suspect in each player's hand
        suspect_counts = {}
        for j in range(num_suspects):
            suspect_counts[chr(j + 65)] = 0

        # Update the dictionary with the number of each suspect in each player's hand
        for j in range(num_suspects):
            if suspects[0] == chr(j + 65):
                suspect_counts[suspects[0]] += 1
            if suspects[1] == chr(j + 65):
                suspect_counts[suspects[1]] += 1

        # Initialize a list to store the possible solutions
        solutions = []

        # Iterate through each possible solution and check if it is admissible
        for j in range(num_suspects - num_circle + 1):
            solution = []
            for k in range(num_circle):
                solution.append(chr(j + k + 65))
            if solution[0] not in suspect_counts or solution[1] not in suspect_counts or solution[2] not in suspect_counts:
                continue
            if solution[0] in suspect_counts and suspect_counts[solution[0]] < reply:
                continue
            if solution[1] in suspect_counts and suspect_counts[solution[1]] < reply:
                continue
            if solution[2] in suspect_counts and suspect_counts[solution[2]] < reply:
                continue
            solutions.append(solution)

        # Update the number of solutions
        num_solutions += len(solutions)

    return num_solutions

