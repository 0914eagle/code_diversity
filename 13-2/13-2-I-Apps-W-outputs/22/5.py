
def get_highest_score(n, m, a):
    # Calculate the average score of the class
    average = sum(a) / n

    # Initialize the highest possible score for student 1
    highest_score = 0

    # Iterate through all possible scores for student 1
    for i in range(m + 1):
        # Calculate the new average score if student 1 gets score i
        new_average = (average * n - a[0] + i) / n

        # Check if the new average is an integer and if it satisfies the condition that the average score of the class doesn't change
        if new_average % 1 == 0 and new_average >= average:
            highest_score = max(highest_score, i)

    return highest_score

