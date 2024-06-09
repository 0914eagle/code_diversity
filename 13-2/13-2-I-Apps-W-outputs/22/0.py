
def get_highest_score(n, m, a):
    # Calculate the average score of the class
    average = sum(a) / n

    # Sort the array in descending order
    a.sort(reverse=True)

    # Initialize the highest possible score to be the maximum score
    highest_score = m

    # Loop through the array and find the first index where the score is less than or equal to the average
    for i in range(n):
        if a[i] <= average:
            highest_score = a[i]
            break

    return highest_score

