
def get_optimal_time(t_s, t_f, t, n, visitors):
    # Find the earliest time that Vasya can arrive to be served
    earliest_time = t_s
    for visitor in visitors:
        if visitor < earliest_time:
            earliest_time = visitor

    # Find the latest time that Vasya can arrive to be served
    latest_time = t_f - 1
    for visitor in visitors:
        if visitor > latest_time:
            latest_time = visitor

    # Initialize the optimal time to be the earliest time
    optimal_time = earliest_time

    # Iterate through all possible times between the earliest and latest times
    for time in range(earliest_time, latest_time + 1):
        # Calculate the total time Vasya spends in the queue
        total_time = 0
        for visitor in visitors:
            if visitor > time:
                total_time += t

        # If the total time is less than the current optimal time, update the optimal time
        if total_time < optimal_time:
            optimal_time = total_time

    return optimal_time

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = [int(x) for x in input().split()]
    print(get_optimal_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

