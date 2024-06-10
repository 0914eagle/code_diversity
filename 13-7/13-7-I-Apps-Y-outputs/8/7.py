
def get_original_length(n, p, k, timestamps):
    original_length = 0
    for i in range(n):
        segment_length = (timestamps[i] - original_length) / (100 + i * p)
        original_length += segment_length
    return original_length

def get_input():
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    return n, p, k, timestamps

def main():
    n, p, k, timestamps = get_input()
    original_length = get_original_length(n, p, k, timestamps)
    print(original_length)

if __name__ == '__main__':
    main()

