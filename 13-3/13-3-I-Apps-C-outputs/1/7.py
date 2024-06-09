
def black_vienna(investigations):
    num_investigations = len(investigations)
    num_suspects = 26
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

        # Check if the reply is consistent with the number of each suspect in each player's hand
        if suspect_counts[suspects[0]] + suspect_counts[suspects[1]] == reply:
            num_solutions += 1

    return num_solutions

