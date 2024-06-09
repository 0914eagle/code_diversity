
def get_min_distance_and_pairs(coordinates):
    # Sort the coordinates in ascending order
    sorted_coordinates = sorted(coordinates)

    # Initialize the minimum distance and quantity of pairs
    min_distance = float('inf')
    quantity_of_pairs = 0

    # Iterate over the sorted coordinates
    for i in range(len(sorted_coordinates)):
        for j in range(i+1, len(sorted_coordinates)):
            # Calculate the distance between the current pair of cities
            distance = abs(sorted_coordinates[i] - sorted_coordinates[j])

            # If the distance is less than the minimum distance, update the minimum distance and quantity of pairs
            if distance < min_distance:
                min_distance = distance
                quantity_of_pairs = 1
            # If the distance is equal to the minimum distance, increment the quantity of pairs
            elif distance == min_distance:
                quantity_of_pairs += 1

    return min_distance, quantity_of_pairs

