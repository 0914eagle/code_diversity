
def f1(N, K, circle):
    # Initialize a dictionary to store the number of occurrences of each starting circle
    circle_count = {}

    # Iterate through all possible starting circles
    for i in range(N):
        # Initialize a list to store the current circle
        current_circle = []

        # Add the ith pebble to the current circle
        current_circle.append(circle[i])

        # Iterate through the remaining pebbles
        for j in range(i+1, N):
            # Add the jth pebble to the current circle
            current_circle.append(circle[j])

            # Check if the current circle has already been encountered
            if tuple(current_circle) in circle_count:
                # Increment the number of occurrences of the current circle
                circle_count[tuple(current_circle)] += 1
            else:
                # Add the current circle to the dictionary with an occurrence count of 1
                circle_count[tuple(current_circle)] = 1

    # Return the number of distinct starting circles
    return len(circle_count)

def f2(N, K, circle):
    # Initialize a dictionary to store the number of occurrences of each starting circle
    circle_count = {}

    # Iterate through all possible starting circles
    for i in range(N):
        # Initialize a list to store the current circle
        current_circle = []

        # Add the ith pebble to the current circle
        current_circle.append(circle[i])

        # Iterate through the remaining pebbles
        for j in range(i+1, N):
            # Add the jth pebble to the current circle
            current_circle.append(circle[j])

            # Check if the current circle has already been encountered
            if tuple(current_circle) in circle_count:
                # Increment the number of occurrences of the current circle
                circle_count[tuple(current_circle)] += 1
            else:
                # Add the current circle to the dictionary with an occurrence count of 1
                circle_count[tuple(current_circle)] = 1

    # Return the number of distinct starting circles
    return len(circle_count)

if __name__ == '__main__':
    N, K = map(int, input().split())
    circle = input()
    print(f1(N, K, circle))
    print(f2(N, K, circle))

