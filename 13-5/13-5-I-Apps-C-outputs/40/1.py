
def f1(N, K, circle):
    # Initialize a dictionary to store the number of occurrences of each starting circle
    circle_count = {}

    # Iterate over the possible starting circles
    for i in range(N):
        # Initialize a list to store the current circle
        current_circle = []

        # Iterate over the possible colors
        for j in range(2):
            # Add the current color to the current circle
            current_circle.append(circle[i % N])

            # Update the number of occurrences of the current circle
            if tuple(current_circle) not in circle_count:
                circle_count[tuple(current_circle)] = 1
            else:
                circle_count[tuple(current_circle)] += 1

            # Rotate the current circle
            current_circle = current_circle[1:] + current_circle[:1]

    # Return the number of possible distinct starting circles
    return len(circle_count)

def f2(N, K, circle):
    # Initialize a dictionary to store the number of occurrences of each starting circle
    circle_count = {}

    # Iterate over the possible starting circles
    for i in range(N):
        # Initialize a list to store the current circle
        current_circle = []

        # Iterate over the possible colors
        for j in range(2):
            # Add the current color to the current circle
            current_circle.append(circle[i % N])

            # Update the number of occurrences of the current circle
            if tuple(current_circle) not in circle_count:
                circle_count[tuple(current_circle)] = 1
            else:
                circle_count[tuple(current_circle)] += 1

            # Rotate the current circle
            current_circle = current_circle[1:] + current_circle[:1]

    # Return the number of possible distinct starting circles
    return len(circle_count)

if __name__ == '__main__':
    N, K = map(int, input().split())
    circle = list(input())
    print(f1(N, K, circle))
    print(f2(N, K, circle))

