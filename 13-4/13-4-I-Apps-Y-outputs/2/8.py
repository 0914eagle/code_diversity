
def get_intervals(n):
    intervals = []
    for i in range(n):
        a, b = map(int, input().split())
        intervals.append((a, b))
    return intervals

def is_pot_boiling_at_same_time(intervals):
    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])
    
    # Initialize the current time to 0
    current_time = 0
    
    # Iterate through the intervals and check if the pot is boiling at the same time
    for interval in intervals:
        # If the current time is within the interval, the pot is boiling
        if current_time >= interval[0] and current_time <= interval[1]:
            return "edward is right"
        # Otherwise, the current time is not within the interval, so move the current time to the end of the interval
        current_time = interval[1]
    
    # If the loop completes and the pot is not boiling at the same time, return "gunilla has a point"
    return "gunilla has a point"

def main():
    n = int(input())
    intervals = get_intervals(n)
    print(is_pot_boiling_at_same_time(intervals))

if __name__ == '__main__':
    main()

