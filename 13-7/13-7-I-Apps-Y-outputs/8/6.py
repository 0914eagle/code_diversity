
def get_speed_up(p, k, n, timestamps):
    speed_up = 0
    for i in range(n):
        speed_up += (timestamps[i] - speed_up) * (100 + p) / 100
    return speed_up

def get_original_length(p, k, n, timestamps):
    speed_up = get_speed_up(p, k, n, timestamps)
    return k - speed_up

def main():
    n, p, k = map(int, input().split())
    timestamps = list(map(int, input().split()))
    print(get_original_length(p, k, n, timestamps))

if __name__ == '__main__':
    main()

