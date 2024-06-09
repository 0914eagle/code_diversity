
def solve(n, answers):
    # Initialize the count of correct answers for each boy
    adrian_count = 0
    bruno_count = 0
    goran_count = 0

    # Iterate through the answers
    for i, answer in enumerate(answers):
        # Get the correct answer for the current question
        correct_answer = answers[i]

        # Update the count of correct answers for each boy
        if answer == correct_answer:
            adrian_count += 1
        if (i % 2 == 0 and answer == "A") or (i % 2 == 1 and answer == "B"):
            bruno_count += 1
        if (i % 2 == 0 and answer == "C") or (i % 2 == 1 and answer == "A"):
            goran_count += 1

    # Find the boy with the most correct answers
    max_count = max(adrian_count, bruno_count, goran_count)
    if max_count == adrian_count:
        return "Adrian"
    elif max_count == bruno_count:
        return "Bruno"
    else:
        return "Goran"

