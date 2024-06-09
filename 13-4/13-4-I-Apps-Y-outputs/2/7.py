
def f1(n, intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the intervals
    for interval in intervals:
        # If the current time is within the interval, move the current time to the end of the interval
        if current_time >= interval[0] and current_time <= interval[1]:
            current_time = interval[1]

        # If the current time is after the interval, move the current time to the end of the interval
        elif current_time > interval[1]:
            current_time = interval[1]

        # If the current time is before the interval, move the current time to the start of the interval
        else:
            current_time = interval[0]

    # If the current time is equal to the total time, return "edward is right"
    if current_time == sum(interval[1] for interval in intervals):
        return "edward is right"

    # Otherwise, return "gunilla has a point"
    else:
        return "gunilla has a point"

def f2(n, intervals):
    # Initialize the start and end times of the intervals
    start_times = [interval[0] for interval in intervals]
    end_times = [interval[1] for interval in intervals]

    # Sort the start times
    start_times.sort()

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the start times
    for start_time in start_times:
        # If the current time is within the interval, move the current time to the end of the interval
        if current_time >= start_time and current_time <= end_times[start_times.index(start_time)]:
            current_time = end_times[start_times.index(start_time)]

        # If the current time is after the interval, move the current time to the end of the interval
        elif current_time > end_times[start_times.index(start_time)]:
            current_time = end_times[start_times.index(start_time)]

        # If the current time is before the interval, move the current time to the start of the interval
        else:
            current_time = start_time

    # If the current time is equal to the total time, return "edward is right"
    if current_time == sum(end_times):
        return "edward is right"

    # Otherwise, return "gunilla has a point"
    else:
        return "gunilla has a point"

if __name__ == '__main__':
    n = int(input())
    intervals = []

    for _ in range(n):
        a, b = map(int, input().split())
        intervals.append([a, b])

    print(f1(n, intervals))
    print(f2(n, intervals))

