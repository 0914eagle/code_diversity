
def max_points(a):
    # Sort the list in ascending order
    a.sort()
    # Initialize variables to keep track of points and current element
    points, current = 0, 1
    # Iterate through the list
    for i in range(len(a)):
        # If the current element is equal to the previous element, skip it
        if a[i] == current:
            continue
        # Otherwise, add the points for the current element and update the current element
        points += a[i]
        current = a[i]
    return points

