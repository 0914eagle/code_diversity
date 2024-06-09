
def get_highest_score(n, m, a):
    # Calculate the average score of the class
    average = sum(a) / n

    # Initialize the highest possible score for student 1
    highest_score = 0

    # Iterate through all possible scores for student 1
    for i in range(m + 1):
        # Calculate the new average score if student 1 gets score i
        new_average = (average * n - a[0] + i) / n

        # Check if the new average is an integer and if it is greater than the current highest possible score
        if new_average % 1 == 0 and new_average > highest_score:
            highest_score = new_average

    return int(highest_score)

