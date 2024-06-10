
def get_good_sleeping_times(n, h, l, r, a):
    good_times = 0
    current_time = 0
    for i in range(n):
        if current_time + a[i] <= h:
            current_time += a[i]
            if l <= current_time <= r:
                good_times += 1
        else:
            current_time = a[i] - 1
    return good_times

def get_optimal_sleeping_times(n, h, l, r, a):
    optimal_times = 0
    for i in range(n):
        if a[i] - 1 <= h - l:
            optimal_times += 1
    return optimal_times

if __name__ == '__main__':
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_optimal_sleeping_times(n, h, l, r, a))

