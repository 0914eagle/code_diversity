
def find_min_progressions(a):
    # Initialize variables
    n = len(a)
    progressions = 0
    current_progression = []

    # Iterate through the array
    for i in range(n):
        # If the current element is -1, skip it
        if a[i] == -1:
            continue
        # If the current element is not -1, add it to the current progression
        current_progression.append(a[i])
        # If the current progression is not empty and the next element is -1, add the current progression to the total number of progressions
        if i < n-1 and a[i+1] == -1:
            progressions += 1
            current_progression = []

    # If the current progression is not empty, add it to the total number of progressions
    if current_progression:
        progressions += 1

    return progressions

