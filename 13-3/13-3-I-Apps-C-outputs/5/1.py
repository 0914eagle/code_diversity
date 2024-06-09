
def solve(n, q, houses, requests):
    # Initialize a dictionary to store the coordinates of each house
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
            # Get the coordinates of the current house
            x, y = house_coords[house]

            # Iterate over each other house in the request
            for other_house in range(start, end+1):
                # If the current house is not the same as the other house
                if house != other_house:
                    # Get the coordinates of the other house
                    x2, y2 = house_coords[other_house]

                    # Calculate the distance between the two houses
                    distance = ((x-x2)**2 + (y-y2)**2)**0.5

                    # If the distance is less than the minimum side length, update the minimum side length
                    if distance < min_side_length:
                        min_side_length = distance

        # Add the minimum side length to the list of answers
        answers.append(min_side_length)

    return answers

