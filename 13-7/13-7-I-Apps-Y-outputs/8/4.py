
def get_original_length(n, p, k, timestamps):
    # Initialize the original length as the total length of the video
    original_length = k
    # Iterate through the timestamps and adjust the original length accordingly
    for i in range(n):
        original_length -= (timestamps[i] * (100 + p) / 100)
    return original_length

def main():
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    original_length = get_original_length(n, p, k, timestamps)
    print(original_length)

if __name__ == '__main__':
    main()

