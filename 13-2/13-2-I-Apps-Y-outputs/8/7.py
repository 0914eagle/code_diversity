
def solve(n, answers):
    # Initialize variables
    adrian_seq = "A" * n
    bruno_seq = "B" * n
    goran_seq = "C" * n
    max_correct = 0
    winners = []

    # Loop through each question
    for i in range(n):
        # Check which sequence has the correct answer
        if answers[i] == "A":
            adrian_seq = adrian_seq.replace("A", "B", 1)
            bruno_seq = bruno_seq.replace("B", "C", 1)
            goran_seq = goran_seq.replace("C", "A", 1)
        elif answers[i] == "B":
            adrian_seq = adrian_seq.replace("A", "C", 1)
            bruno_seq = bruno_seq.replace("B", "A", 1)
            goran_seq = goran_seq.replace("C", "B", 1)
        else:
            adrian_seq = adrian_seq.replace("A", "B", 1)
            bruno_seq = bruno_seq.replace("B", "C", 1)
            goran_seq = goran_seq.replace("C", "A", 1)

        # Count the number of correct answers for each sequence
        adrian_correct = adrian_seq.count("A")
        bruno_correct = bruno_seq.count("B")
        goran_correct = goran_seq.count("C")

        # Update the maximum number of correct answers
        max_correct = max(max_correct, adrian_correct, bruno_correct, goran_correct)

        # Add the winners to the list
        if adrian_correct == max_correct:
            winners.append("Adrian")
        if bruno_correct == max_correct:
            winners.append("Bruno")
        if goran_correct == max_correct:
            winners.append("Goran")

    # Return the maximum number of correct answers and the winners
    return max_correct, sorted(winners)

