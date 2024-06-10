
def get_original_length(n, p, k, timestamps):
    # Initialize the original length as the total length of the video
    original_length = k
    # Iterate through the timestamps and update the original length
    for i in range(n):
        # Get the current timestamp and the previous timestamp
        current_timestamp = timestamps[i]
        previous_timestamp = timestamps[i-1] if i > 0 else 0
        # Calculate the length of the current segment
        current_segment_length = current_timestamp - previous_timestamp
        # Update the original length by subtracting the length of the current segment and adding the length of the current segment at the original speed
        original_length -= current_segment_length
        original_length += current_segment_length / (100 + p)
    # Return the original length
    return original_length

def main():
    # Read the input
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    # Call the function to get the original length
    original_length = get_original_length(n, p, k, timestamps)
    # Print the output
    print(original_length)

if __name__ == '__main__':
    main()

