
def solve(n, q, houses, requests):
    # Initialize a dictionary to store the x and y coordinates of each house
    house_coords = {}
    for i in range(n):
        house_coords[i+1] = (houses[i][0], houses[i][1])

    # Initialize a list to store the answers for each request
    answers = []

    # Iterate over each request
    for request in requests:
        # Get the start and end addresses of the request
        start, end = request[0], request[1]

        # Initialize the minimum side length to infinity
        min_side_length = float('inf')

        # Iterate over each house in the request
        for house in range(start, end+1):
            # Get the x and y coordinates of the current house
            x, y = house_coords[house]

            # Iterate over each other house in the request
            for other_house in range(start, end+1):
                # If the current house is not the same as the other house
                if house != other_house:
                    # Get the x and y coordinates of the other house
                    other_x, other_y = house_coords[other_house]

                    # Calculate the distance between the current house and the other house
                    distance = abs(x - other_x) + abs(y - other_y)

                    # Update the minimum side length if necessary
                    min_side_length = min(min_side_length, distance)

        # Add the minimum side length to the list of answers
        answers.append(min_side_length)

    return answers

