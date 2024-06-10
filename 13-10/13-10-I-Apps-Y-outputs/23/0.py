
def get_correct_answers(correct_answers):
    # Initialize a dictionary to store the number of correct answers for each boy
    correct_answers_dict = {"Adrian": 0, "Bruno": 0, "Goran": 0}

    # Iterate through the correct answers list
    for i, answer in enumerate(correct_answers):
        # Get the current answer
        current_answer = answer

        # Get the current boy's sequence
        adrian_sequence = "A" if i % 3 == 0 else "B" if i % 3 == 1 else "C"
        bruno_sequence = "B" if i % 3 == 0 else "A" if i % 3 == 1 else "C"
        goran_sequence = "C" if i % 3 == 0 else "A" if i % 3 == 1 else "B"

        # Check if the current answer is correct for each boy's sequence
        if current_answer == adrian_sequence:
            correct_answers_dict["Adrian"] += 1
        if current_answer == bruno_sequence:
            correct_answers_dict["Bruno"] += 1
        if current_answer == goran_sequence:
            correct_answers_dict["Goran"] += 1

    # Return the boy with the highest number of correct answers
    max_correct_answers = max(correct_answers_dict.values())
    boys_with_max_correct_answers = [
        boy for boy, num_correct_answers in correct_answers_dict.items() if num_correct_answers == max_correct_answers
    ]
    return boys_with_max_correct_answers

def main():
    # Get the number of questions
    num_questions = int(input())

    # Get the correct answers list
    correct_answers = input()

    # Call the get_correct_answers function
    boys_with_max_correct_answers = get_correct_answers(correct_answers)

    # Print the result
    print(len(boys_with_max_correct_answers))
    print(" ".join(sorted(boys_with_max_correct_answers)))

if __name__ == "__main__":
    main()

