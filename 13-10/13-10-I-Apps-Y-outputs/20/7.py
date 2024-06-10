
def get_good_sleeping_times(a, l, r, n, h):
    good_times = 0
    current_time = 0
    for i in range(n):
        if current_time + a[i] - 1 <= r and current_time + a[i] >= l:
            good_times += 1
        current_time = (current_time + a[i]) % h
    return good_times

def main():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_good_sleeping_times(a, l, r, n, h))

if __name__ == '__main__':
    main()

