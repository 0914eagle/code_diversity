
def solve(n, answers):
    # Initialize variables
    adrian_seq = "A" * n
    bruno_seq = "B" * n
    goran_seq = "C" * n
    correct_answers = 0

    # Loop through the answers and count the number of correct answers for each sequence
    for i in range(n):
        if adrian_seq[i] == answers[i]:
            correct_answers += 1
        if bruno_seq[i] == answers[i]:
            correct_answers += 1
        if goran_seq[i] == answers[i]:
            correct_answers += 1

    # Return the number of correct answers and the names of the boys whose sequences result in the most correct answers
    return correct_answers, "Adrian", "Bruno", "Goran"

