
def read_input():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    return n, h, l, r, a

def is_good_time(time, l, r):
    return l <= time <= r

def optimal_sleep_schedule(n, h, l, r, a):
    good_times = 0
    current_time = 0
    for i in range(n):
        if is_good_time(current_time, l, r):
            good_times += 1
        current_time += a[i]
        if current_time >= h:
            current_time -= h
    return good_times

def main():
    n, h, l, r, a = read_input()
    print(optimal_sleep_schedule(n, h, l, r, a))

if __name__ == '__main__':
    main()

