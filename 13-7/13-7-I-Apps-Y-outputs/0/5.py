
def is_triangle_possible(stick_lengths):
    # Sort the stick lengths in descending order
    stick_lengths.sort(reverse=True)

    # Check if the longest stick is greater than the sum of the other two sticks
    if stick_lengths[0] > stick_lengths[1] + stick_lengths[2]:
        return "possible"
    else:
        return "impossible"

