
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
        if answer == correct_answer:
            bruno_count += 1
        if answer == correct_answer:
            goran_count += 1

    # Find the boy with the most correct answers
    max_count = max(adrian_count, bruno_count, goran_count)
    if max_count == adrian_count:
        return "Adrian"
    if max_count == bruno_count:
        return "Bruno"
    if max_count == goran_count:
        return "Goran"

n = int(input())
answers = input()
print(solve(n, answers))

