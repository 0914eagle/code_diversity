
def get_absurdity_value(n, k, x):
    # Calculate the total absurdity value for each segment
    total_absurdity = [0] * (n - k + 1)
    for i in range(n):
        total_absurdity[i] += x[i]
        if i + k < n:
            total_absurdity[i + 1] -= x[i]

    # Find the maximum total absurdity value
    max_absurdity = max(total_absurdity)

    # Find the segments with the maximum total absurdity value
    segments = []
    for i in range(n - k + 1):
        if total_absurdity[i] == max_absurdity:
            segments.append(i)

    return segments

def get_optimal_segments(n, k, x):
    # Get the absurdity value for each law
    absurdity = [0] * n
    for i in range(n):
        absurdity[i] = x[i]

    # Sort the laws by absurdity value in descending order
    sorted_laws = sorted(enumerate(absurdity), key=lambda x: x[1], reverse=True)

    # Initialize the optimal segments
    optimal_segments = []

    # Iterate through the sorted laws and add them to the optimal segments
    for i, law in sorted_laws:
        # Check if the current law is already in an optimal segment
        in_optimal_segment = False
        for segment in optimal_segments:
            if i in segment:
                in_optimal_segment = True
                break

        # If the current law is not in an optimal segment, add it to a new segment
        if not in_optimal_segment:
            optimal_segments.append([i])

        # If the current law is in an optimal segment, add it to that segment
        else:
            for segment in optimal_segments:
                if i in segment:
                    segment.append(i)
                    break

    # Return the optimal segments
    return optimal_segments

def get_sign_segments(n, k, x):
    # Get the optimal segments
    optimal_segments = get_optimal_segments(n, k, x)

    # Initialize the sign segments
    sign_segments = []

    # Iterate through the optimal segments and add them to the sign segments
    for segment in optimal_segments:
        sign_segments.append(segment)

    # Return the sign segments
    return sign_segments

def main():
    # Read the input
    n, k = map(int, input().split())
    x = list(map(int, input().split()))

    # Get the sign segments
    sign_segments = get_sign_segments(n, k, x)

    # Print the sign segments
    print(sign_segments[0][0], sign_segments[1][0])

if __name__ == '__main__':
    main()

