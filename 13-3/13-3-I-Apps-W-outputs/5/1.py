
def get_optimal_time(t_s, t_f, t, n, visitors):
    # Find the earliest time that Vasya can arrive to be served
    earliest_time = max(visitors)

    # Find the latest time that Vasya can arrive to be served
    latest_time = t_f - t

    # Initialize the minimum time Vasya has to wait in the queue
    min_time = float('inf')

    # Iterate through all possible times Vasya can arrive
    for time in range(earliest_time, latest_time + 1):
        # Calculate the time Vasya has to wait in the queue
        time_waiting = 0
        for visitor in visitors:
            if visitor > time:
                time_waiting += t
            else:
                break

        # Update the minimum time Vasya has to wait in the queue
        min_time = min(min_time, time_waiting)

    return earliest_time + min_time

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = [int(x) for x in input().split()]
    print(get_optimal_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

