
def get_intervals(n):
    intervals = []
    for i in range(n):
        a, b = map(int, input().split())
        intervals.append([a, b])
    return intervals

def is_pot_boiling_at_same_time(intervals):
    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])
    
    # Initialize the current time to 0
    current_time = 0
    
    # Iterate through the intervals and check if the pot is boiling at the same time
    for interval in intervals:
        if interval[0] > current_time:
            # If the current time is less than the start time of the interval, the pot is not boiling
            return False
        current_time = interval[1]
    
    # If the pot is boiling at the same time for all intervals, return True
    return True

def main():
    n = int(input())
    intervals = get_intervals(n)
    if is_pot_boiling_at_same_time(intervals):
        print("edward is right")
    else:
        print("gunilla has a point")

if __name__ == '__main__':
    main()

