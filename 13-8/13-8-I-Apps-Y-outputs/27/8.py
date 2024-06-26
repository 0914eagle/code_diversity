
def get_good_sleep_times(n, h, l, r, a):
    good_sleep_times = 0
    current_time = 0
    for i in range(n):
        if current_time + a[i] - 1 <= r:
            current_time += a[i] - 1
        else:
            current_time += a[i]
        if current_time >= l and current_time <= r:
            good_sleep_times += 1
    return good_sleep_times

def main():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_good_sleep_times(n, h, l, r, a))

if __name__ == '__main__':
    main()

