
def is_possible_to_choose_three_musketeers(n, m, pairs):
    # Initialize a dictionary to store the recognition of each warrior
    recognitions = {}
    for i in range(1, n + 1):
        recognitions[i] = 0

    # Iterate over the pairs of warriors knowing each other
    for pair in pairs:
        # If the warriors are already known to each other, skip this pair
        if pair[0] in recognitions[pair[1]] or pair[1] in recognitions[pair[0]]:
            continue
        # Increment the recognition of both warriors
        recognitions[pair[0]] += 1
        recognitions[pair[1]] += 1

    # Find the three warriors with the minimum recognition
    min_recognition = float('inf')
    musketeers = []
    for warrior, recognition in recognitions.items():
        if recognition < min_recognition:
            min_recognition = recognition
            musketeers = [warrior]
        elif recognition == min_recognition:
            musketeers.append(warrior)

    # Check if it is possible to choose three musketeers knowing each other
    if len(musketeers) < 3:
        return -1

    # Return the minimum possible sum of recognitions
    return min_recognition * 3

