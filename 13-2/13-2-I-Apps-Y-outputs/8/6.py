
def get_correct_answers(n, correct_answers):
    # Initialize a dictionary to store the number of correct answers for each boy
    correct_answers_dict = {"Adrian": 0, "Bruno": 0, "Goran": 0}

    # Iterate through the correct answers and increment the number of correct answers for each boy
    for i, answer in enumerate(correct_answers):
        if i % 3 == 0:
            # Adrian's sequence
            if answer == "A":
                correct_answers_dict["Adrian"] += 1
        elif i % 3 == 1:
            # Bruno's sequence
            if answer == "B":
                correct_answers_dict["Bruno"] += 1
        else:
            # Goran's sequence
            if answer == "C":
                correct_answers_dict["Goran"] += 1

    # Find the boy with the most correct answers
    max_correct_answers = max(correct_answers_dict.values())
    boys_with_max_correct_answers = [
        boy for boy, num_correct in correct_answers_dict.items() if num_correct == max_correct_answers
    ]

    # Return the number of correct answers and the names of the boys with the most correct answers
    return max_correct_answers, sorted(boys_with_max_correct_answers)

