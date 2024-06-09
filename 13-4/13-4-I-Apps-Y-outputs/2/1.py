
def f1(n, intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current time and the previous interval
    current_time = 0
    previous_interval = [0, 0]

    # Iterate through the intervals
    for interval in intervals:
        # If the current time is within the current interval, update the current time
        if current_time >= interval[0] and current_time <= interval[1]:
            current_time = interval[1]

        # If the current time is greater than the previous interval, update the previous interval
        elif current_time > previous_interval[1]:
            previous_interval = interval

    # If the current time is greater than the previous interval, Edward is right
    if current_time > previous_interval[1]:
        return "edward is right"

    # Otherwise, Gunilla has a point
    else:
        return "gunilla has a point"

def f2(n, intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize the current time and the previous interval
    current_time = 0
    previous_interval = [0, 0]

    # Iterate through the intervals
    for interval in intervals:
        # If the current time is within the current interval, update the current time
        if current_time >= interval[0] and current_time <= interval[1]:
            current_time = interval[1]

        # If the current time is greater than the previous interval, update the previous interval
        elif current_time > previous_interval[1]:
            previous_interval = interval

    # If the current time is greater than the previous interval, Gunilla has a point
    if current_time > previous_interval[1]:
        return "gunilla has a point"

    # Otherwise, Edward is right
    else:
        return "edward is right"

if __name__ == '__main__':
    n = int(input())
    intervals = []
    for _ in range(n):
        a, b = map(int, input().split())
        intervals.append([a, b])
    print(f1(n, intervals))
    print(f2(n, intervals))

