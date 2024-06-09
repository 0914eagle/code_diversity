
def get_min_progressions(a):
    # Initialize variables
    progressions = 0
    current_progression = []

    # Iterate through the array
    for i in range(len(a)):
        # If the current element is -1, add it to the current progression
        if a[i] == -1:
            current_progression.append(a[i])
        # If the current element is not -1, start a new progression
        else:
            # If the current progression is not empty, add it to the total number of progressions
            if current_progression:
                progressions += 1
            # Start a new progression with the current element
            current_progression = [a[i]]

    # If the last progression is not empty, add it to the total number of progressions
    if current_progression:
        progressions += 1

    return progressions

