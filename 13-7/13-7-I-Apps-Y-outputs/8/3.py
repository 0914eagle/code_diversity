
def get_original_length(n, p, k, timestamps):
    # Initialize the original length as the total length of the video
    original_length = k
    # Loop through each timestamp
    for i in range(n):
        # Calculate the speedup factor for each segment
        speedup_factor = 1 + (i + 1) * p / 100
        # Calculate the length of the current segment
        segment_length = timestamps[i + 1] - timestamps[i]
        # Update the original length by subtracting the length of the current segment and multiplying by the speedup factor
        original_length -= segment_length / speedup_factor
    return original_length

def main():
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    print(get_original_length(n, p, k, timestamps))

if __name__ == '__main__':
    main()

