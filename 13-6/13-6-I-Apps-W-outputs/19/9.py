
def get_min_distance(coordinates):
    # Sort the coordinates in ascending order
    sorted_coordinates = sorted(coordinates)

    # Initialize the minimum distance and quantity of pairs
    min_distance = float('inf')
    quantity = 0

    # Iterate over the sorted coordinates
    for i in range(len(sorted_coordinates)):
        for j in range(i+1, len(sorted_coordinates)):
            # Calculate the distance between the current pair of coordinates
            distance = abs(sorted_coordinates[i] - sorted_coordinates[j])

            # Update the minimum distance and quantity of pairs if necessary
            if distance < min_distance:
                min_distance = distance
                quantity = 1
            elif distance == min_distance:
                quantity += 1

    return min_distance, quantity

