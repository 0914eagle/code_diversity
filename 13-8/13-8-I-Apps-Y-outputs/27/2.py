
def get_good_sleeping_times(n, h, l, r, a):
    good_times = 0
    current_time = 0
    for i in range(n):
        if l <= current_time <= r:
            good_times += 1
        current_time += a[i]
    return good_times

def solve(n, h, l, r, a):
    return max(get_good_sleeping_times(n, h, l, r, a), get_good_sleeping_times(n, h, l, r, [x-1 for x in a]))

if __name__ == '__main__':
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, h, l, r, a))

