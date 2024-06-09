
def get_optimal_time(t_s, t_f, t, n, visitors):
    # Find the earliest time that Vasya can arrive to be served
    earliest_time = max(visitors)

    # Find the latest time that Vasya can arrive to be served
    latest_time = t_f - t

    # Initialize the minimum time spent in the queue to be the maximum possible time
    min_time_in_queue = float('inf')

    # Iterate through all possible times that Vasya can arrive
    for time in range(earliest_time, latest_time + 1):
        # Calculate the time spent in the queue for this time
        time_in_queue = 0
        for visitor in visitors:
            if visitor > time:
                time_in_queue += t
        # If the time spent in the queue is less than the minimum, update the minimum
        if time_in_queue < min_time_in_queue:
            min_time_in_queue = time_in_queue

    # Return the time that Vasya should arrive to be served
    return earliest_time + min_time_in_queue

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = [int(x) for x in input().split()]
    print(get_optimal_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

