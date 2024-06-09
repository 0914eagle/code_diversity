
def f1(intervals):
    # Sort the intervals by their start time
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
    
    # Return the current time, which is the time at which the pot started boiling
    return current_time

def f2(intervals):
    # Sort the intervals by their start time
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
    
    # Return the current time, which is the time at which the pot started boiling
    return current_time

if __name__ == '__main__':
    n = int(input())
    intervals = []
    for i in range(n):
        a, b = map(int, input().split())
        intervals.append([a, b])
    if f1(intervals) == f2(intervals):
        print("edward is right")
    else:
        print("gunilla has a point")

