
def get_good_sleeping_times(a, l, r, n):
    good_times = 0
    current_time = 0
    for i in range(n):
        if l <= current_time <= r:
            good_times += 1
        current_time += a[i]
    return good_times

def get_max_good_sleeping_times(a, l, r, n):
    max_good_times = 0
    for i in range(n):
        current_time = a[i]
        if l <= current_time <= r:
            max_good_times += 1
        current_time += a[i]
    return max_good_times

if __name__ == '__main__':
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_max_good_sleeping_times(a, l, r, n))

