
def get_player_label(box_player_label, questions):
    # Initialize variables
    current_player_label = box_player_label
    previous_player_label = None

    # Iterate through the questions
    for question in questions:
        # If the answer is true or false, pass the box to the next player
        if question[1] == "T" or question[1] == "N":
            current_player_label = (current_player_label % 8) + 1
        # If the answer is skipped, do not pass the box to the next player
        else:
            pass

        # If the current player label is the same as the previous player label, the box has exploded
        if current_player_label == previous_player_label:
            return current_player_label

        # Update the previous player label
        previous_player_label = current_player_label

    # If the box has not exploded, return the current player label
    return current_player_label

def main():
    # Read the input
    box_player_label, num_questions = map(int, input().split())
    questions = []
    for _ in range(num_questions):
        questions.append(list(map(int, input().split())))

    # Get the player label when the box exploded
    exploded_player_label = get_player_label(box_player_label, questions)

    # Print the output
    print(exploded_player_label)

if __name__ == '__main__':
    main()

