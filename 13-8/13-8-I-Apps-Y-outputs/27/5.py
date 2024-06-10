
def get_good_sleeping_times(n, h, l, r, a):
    good_times = 0
    current_time = 0
    for i in range(n):
        if current_time + a[i] - 1 >= l and current_time + a[i] - 1 <= r:
            good_times += 1
        current_time += a[i]
    return good_times

def main():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_good_sleeping_times(n, h, l, r, a))

if __name__ == '__main__':
    main()

