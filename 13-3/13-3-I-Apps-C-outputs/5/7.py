
def get_min_square_side(points):
    # Sort the points by their x-coordinate
    points.sort(key=lambda x: x[0])

    # Initialize the minimum side length to the x-coordinate of the last point
    min_side = points[-1][0]

    # Iterate through the points and calculate the minimum side length
    for i in range(len(points) - 1):
        # Calculate the distance between the current point and the next point
        dist = points[i + 1][0] - points[i][0]

        # If the distance is less than the current minimum side length, update the minimum side length
        if dist < min_side:
            min_side = dist

    return min_side

def solve(n, q, points, requests):
    # Initialize an empty list to store the answers
    answers = []

    # Iterate through the requests
    for a, b in requests:
        # Extract the points for the current request
        request_points = points[a - 1:b]

        # Calculate the minimum side length of the smallest axis-aligned square that contains all of the points
        min_side = get_min_square_side(request_points)

        # Add the answer to the list of answers
        answers.append(min_side)

    return answers

n, q = map(int, input().split())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
requests = []
for i in range(q):
    a, b = map(int, input().split())
    requests.append((a, b))
answers = solve(n, q, points, requests)
for answer in answers:
    print(answer)

