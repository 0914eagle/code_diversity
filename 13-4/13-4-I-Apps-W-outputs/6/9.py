
def get_min_time(t_s, t_f, t, n, visitors):
    # Find the earliest time that Vasya can arrive to be served
    min_time = t_s
    for visitor in visitors:
        if visitor >= min_time:
            min_time = visitor
    return min_time

def get_max_time(t_s, t_f, t, n, visitors):
    # Find the latest time that Vasya can arrive to be served
    max_time = t_f - 1
    for visitor in visitors:
        if visitor <= max_time:
            max_time = visitor
    return max_time

def get_optimal_time(t_s, t_f, t, n, visitors):
    # Binary search to find the optimal time for Vasya to arrive
    min_time = t_s
    max_time = t_f - 1
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        if is_optimal_time(t_s, t_f, t, n, visitors, mid_time):
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
    return min_time

def is_optimal_time(t_s, t_f, t, n, visitors, time):
    # Check if the given time is optimal for Vasya to arrive
    queue_time = 0
    for visitor in visitors:
        if visitor <= time:
            queue_time += t
    return queue_time == (time - t_s) * n

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = sorted([int(x) for x in input().split()])
    print(get_optimal_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

