
def calculate_original_length(n, p, k):
    # Initialize the original length as the total length of the video
    original_length = k
    # Loop through each event timestamp
    for i in range(n):
        # Calculate the speedup for the current event
        speedup = 100 + p * i
        # Calculate the length of the current segment
        segment_length = (k - (i * speedup / 100)) / (100 - speedup)
        # Subtract the length of the current segment from the original length
        original_length -= segment_length
    # Return the original length
    return original_length

def main():
    # Read the input
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    # Calculate the original length
    original_length = calculate_original_length(n, p, k)
    # Print the result
    print(original_length)

if __name__ == '__main__':
    main()

