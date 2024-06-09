
def insert_interval(intervals, new_interval):
    
    # check if the new interval overlaps with the current interval
    for i in range(len(intervals)):
        interval = intervals[i]
        if new_interval[0] <= interval[1]:
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
            intervals.pop(i)
            break
    # insert the new interval into the list
    intervals.append(new_interval)
    # sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])
    return intervals

