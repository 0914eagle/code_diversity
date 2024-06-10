
def get_good_sleeping_times(a, l, r, n):
    good_times = 0
    current_time = 0
    for i in range(n):
        if l <= current_time <= r:
            good_times += 1
        current_time += a[i]
    return good_times

def solve(n, h, l, r, a):
    return get_good_sleeping_times(a, l, r, n)

if __name__ == '__main__':
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, h, l, r, a))

