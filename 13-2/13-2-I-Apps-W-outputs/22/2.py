
def get_highest_score(n, m, a):
    # Calculate the current average score
    current_average = sum(a) / n

    # Sort the array in descending order
    a.sort(reverse=True)

    # Initialize the highest possible score
    highest_score = 0

    # Loop through the array and find the highest possible score
    for i in range(n):
        # Calculate the new average score if current student gets the highest score
        new_average = (current_average * (n - i - 1) + a[i] + m) / n

        # Check if the new average is greater than or equal to the current average
        if new_average >= current_average:
            # Update the highest possible score
            highest_score = max(highest_score, a[i] + m - new_average + current_average)

    return highest_score

