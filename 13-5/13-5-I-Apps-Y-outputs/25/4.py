
def solve(box_holder, questions):
    # Initialize variables
    time_passed = 0
    current_player = box_holder
    correct_answers = 0

    # Iterate through the questions
    for question in questions:
        time_passed += question[0]
        if question[1] == "T":
            correct_answers += 1
        elif question[1] == "P":
            break
        current_player = (current_player + 1) % 8

    # Determine the player who had the box when it exploded
    return (current_player + correct_answers) % 8 + 1

