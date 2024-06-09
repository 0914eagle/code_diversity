
def is_triangle_possible(stick_lengths):
    
    # Sort the stick lengths in descending order
    stick_lengths.sort(reverse=True)

    # Initialize variables to track the longest and shortest stick lengths
    longest_stick = stick_lengths[0]
    shortest_stick = stick_lengths[-1]

    # Iterate through the stick lengths and check if they can form a triangle
    for i in range(1, len(stick_lengths) - 1):
        if stick_lengths[i] < longest_stick + shortest_stick:
            return "possible"

    return "impossible"

