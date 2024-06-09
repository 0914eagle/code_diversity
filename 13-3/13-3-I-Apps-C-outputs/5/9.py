
def get_min_square_size(houses, zoning_requests):
    # Initialize a dictionary to store the x and y coordinates of each house
    house_coords = {}
    for i, house in enumerate(houses):
        house_coords[i+1] = house

    # Initialize a list to store the answers for each zoning request
    answers = []

    # Iterate over each zoning request
    for a, b in zoning_requests:
        # Get the x and y coordinates of the first and last house in the range
        first_house = house_coords[a]
        last_house = house_coords[b]

        # Calculate the side length of the smallest square that contains all houses in the range
        side_length = max(abs(first_house[0] - last_house[0]), abs(first_house[1] - last_house[1]))

        # Add the side length to the list of answers
        answers.append(side_length)

    return answers

