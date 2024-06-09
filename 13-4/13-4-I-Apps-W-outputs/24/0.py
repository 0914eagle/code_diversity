
def solve(n, m, pairs):
    # Initialize a dictionary to store the recognition of each warrior
    recognitions = {i: 0 for i in range(1, n + 1)}

    # Loop through each pair of warriors knowing each other
    for a, b in pairs:
        # Increment the recognition of both warriors by 1
        recognitions[a] += 1
        recognitions[b] += 1

    # Find the three warriors with the minimum recognition
    min_recognition = min(recognitions.values())
    musketeers = [k for k, v in recognitions.items() if v == min_recognition]

    # Check if there are three musketeers
    if len(musketeers) == 3:
        # Return the sum of their recognitions
        return sum(recognitions[m] for m in musketeers)
    else:
        # Return -1 if there are not three musketeers
        return -1

