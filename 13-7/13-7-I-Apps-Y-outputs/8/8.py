
def get_original_length(n, p, k, timestamps):
    total_speed_up = 0
    for i in range(n):
        total_speed_up += (timestamps[i] * (100 + p)) / 100
    return k / (100 + total_speed_up)

def main():
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    original_length = get_original_length(n, p, k, timestamps)
    print(original_length)

if __name__ == '__main__':
    main()

