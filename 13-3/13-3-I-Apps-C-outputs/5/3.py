
def solve(n, q, houses, requests):
    # Initialize a dictionary to store the coordinates of the houses
    house_coords = {}
    for i in range(n):
        house_coords[i+1] = (houses[i][0], houses[i][1])

    # Initialize a list to store the answers
    answers = []

    # Iterate over the requests
    for request in requests:
        # Get the start and end addresses of the request
        start, end = request[0], request[1]

        # Find the minimum side length of the square
        min_side_length = float('inf')
        for i in range(start, end+1):
            for j in range(i+1, end+1):
                # Calculate the distance between the two houses
                dist = abs(house_coords[i][0] - house_coords[j][0]) + abs(house_coords[i][1] - house_coords[j][1])

                # Update the minimum side length
                min_side_length = min(min_side_length, dist)

        # Add the answer to the list
        answers.append(min_side_length)

    return answers

