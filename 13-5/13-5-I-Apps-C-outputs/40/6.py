
def f1(N, K, circle):
    # Initialize a dictionary to store the number of occurrences of each starting circle
    circle_count = {}

    # Iterate over the possible starting circles
    for i in range(N):
        # Initialize a list to store the current circle
        current_circle = []

        # Iterate over the possible positions of the starting circle
        for j in range(N):
            # Add the current pebble to the current circle
            current_circle.append(circle[(i + j) % N])

        # Convert the current circle to a string
        current_circle = "".join(current_circle)

        # Increment the number of occurrences of the current circle
        if current_circle in circle_count:
            circle_count[current_circle] += 1
        else:
            circle_count[current_circle] = 1

    # Initialize a set to store the distinct starting circles
    distinct_circles = set()

    # Iterate over the possible starting circles
    for circle in circle_count:
        # If the number of occurrences of the current circle is equal to K, add it to the set of distinct starting circles
        if circle_count[circle] == K:
            distinct_circles.add(circle)

    # Return the number of distinct starting circles
    return len(distinct_circles)

def f2(N, K, circle):
    # Initialize a dictionary to store the number of occurrences of each starting circle
    circle_count = {}

    # Iterate over the possible starting circles
    for i in range(N):
        # Initialize a list to store the current circle
        current_circle = []

        # Iterate over the possible positions of the starting circle
        for j in range(N):
            # Add the current pebble to the current circle
            current_circle.append(circle[(i + j) % N])

        # Convert the current circle to a string
        current_circle = "".join(current_circle)

        # Increment the number of occurrences of the current circle
        if current_circle in circle_count:
            circle_count[current_circle] += 1
        else:
            circle_count[current_circle] = 1

    # Initialize a set to store the distinct starting circles
    distinct_circles = set()

    # Iterate over the possible starting circles
    for circle in circle_count:
        # If the number of occurrences of the current circle is equal to K, add it to the set of distinct starting circles
        if circle_count[circle] == K:
            distinct_circles.add(circle)

    # Return the number of distinct starting circles
    return len(distinct_circles)

if __name__ == '__main__':
    N, K = map(int, input().split())
    circle = input()
    print(f1(N, K, circle))
    print(f2(N, K, circle))

