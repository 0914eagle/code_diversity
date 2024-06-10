
def get_original_length(n, p, k, timestamps):
    # Calculate the length of each segment
    segment_lengths = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    segment_lengths.insert(0, timestamps[0])
    
    # Calculate the total length of the video
    total_length = 0
    for i in range(len(segment_lengths)):
        if i % 2 == 0:
            total_length += segment_lengths[i]
        else:
            total_length += segment_lengths[i] * (100 + p) / 100
    
    return total_length

def main():
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    print(get_original_length(n, p, k, timestamps))

if __name__ == '__main__':
    main()

