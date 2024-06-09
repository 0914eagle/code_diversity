
def get_maximum_grade(scores):
    # Calculate the sum of the scores
    total_score = sum(scores)

    # Check if the total score is a multiple of 10
    if total_score % 10 == 0:
        # If it is, return the total score
        return total_score
    else:
        # If it's not, find the highest multiple of 10 that is lower than the total score
        return (total_score // 10) * 10

