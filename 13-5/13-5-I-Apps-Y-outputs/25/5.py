
def solve(k, n, questions):
    # Initialize a list to store the player numbers
    player_numbers = list(range(1, 9))
    # Remove the player who has the box initially from the list
    player_numbers.remove(k)
    # Iterate through the questions
    for i in range(n):
        # Get the time and answer type for the current question
        time, answer = questions[i]
        # If the answer is true or false, pass the box to the next player
        if answer in ["T", "N"]:
            k = player_numbers[i % 8]
        # If the answer is skipped, skip the current player and pass the box to the next player
        elif answer == "P":
            k = player_numbers[(i + 1) % 8]
    # Return the player number who had the box when it exploded
    return k

