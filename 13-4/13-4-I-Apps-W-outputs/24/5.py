
def find_musketeers(n, m, pairs):
    # Initialize a dictionary to store the recognition of each warrior
    recognitions = {i: 0 for i in range(1, n + 1)}

    # Iterate over the pairs of warriors knowing each other
    for a, b in pairs:
        # Increment the recognition of both warriors
        recognitions[a] += 1
        recognitions[b] += 1

    # Find the three warriors with the minimum recognition
    min_recognition = min(recognitions.values())
    musketeers = [k for k, v in recognitions.items() if v == min_recognition]

    # Check if there are at least three musketeers
    if len(musketeers) < 3:
        return -1

    # Return the sum of the recognitions of the three musketeers
    return sum(recognitions[m] for m in musketeers)

