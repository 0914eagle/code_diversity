
def get_max_points(sequence):
    # Sort the sequence in descending order
    sequence.sort(reverse=True)
    # Initialize variables to keep track of points and unique elements
    points = 0
    unique_elements = set()
    # Iterate through the sequence and check if each element is unique
    for element in sequence:
        if element not in unique_elements:
            points += element
            unique_elements.add(element)
    return points

