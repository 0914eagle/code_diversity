
def get_optimal_time(t_s, t_f, t, n, visitors):
    # Find the earliest time that Vasya can arrive to be served
    earliest_time = max(visitors)

    # Find the latest time that Vasya can arrive to be served
    latest_time = t_f - t

    # Initialize the minimum time spent in the queue to be the maximum possible time
    min_queue_time = float('inf')

    # Iterate through all possible times that Vasya can arrive
    for time in range(earliest_time, latest_time + 1):
        # Calculate the time spent in the queue for this time
        queue_time = 0
        for visitor in visitors:
            if visitor > time:
                queue_time += t
            else:
                break

        # If the current time results in the minimum queue time, update the optimal time
        if queue_time < min_queue_time:
            min_queue_time = queue_time
            optimal_time = time

    return optimal_time

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = [int(x) for x in input().split()]
    print(get_optimal_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

