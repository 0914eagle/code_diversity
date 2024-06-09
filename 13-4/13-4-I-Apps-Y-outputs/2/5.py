
def f1(intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the intervals
    for interval in intervals:
        # If the interval starts after the current time, update the current time
        if interval[0] > current_time:
            current_time = interval[0]

        # If the interval ends after the current time, update the current time
        if interval[1] > current_time:
            current_time = interval[1]

    # If the current time is equal to the total time, return "edward is right"
    if current_time == sum(interval[1] for interval in intervals):
        return "edward is right"

    # Otherwise, return "gunilla has a point"
    return "gunilla has a point"

def f2(intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the intervals
    for interval in intervals:
        # If the interval starts after the current time, update the current time
        if interval[0] > current_time:
            current_time = interval[0]

        # If the interval ends after the current time, update the current time
        if interval[1] > current_time:
            current_time = interval[1]

    # If the current time is equal to the total time, return "edward is right"
    if current_time == sum(interval[1] for interval in intervals):
        return "edward is right"

    # Otherwise, return "gunilla has a point"
    return "gunilla has a point"

if __name__ == '__main__':
    n = int(input())
    intervals = []
    for _ in range(n):
        a, b = map(int, input().split())
        intervals.append([a, b])
    print(f1(intervals))

