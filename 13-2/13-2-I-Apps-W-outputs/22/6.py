
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
        new_average = (current_average * n - a[i] + m) / (n - 1)

        # Check if the new average is an integer
        if new_average % 1 == 0:
            # If it is, update the highest possible score
            highest_score = max(highest_score, m - int(new_average))

    return highest_score

