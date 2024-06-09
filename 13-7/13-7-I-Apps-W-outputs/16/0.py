
def insert_interval(intervals, new_interval):
    
    result = []
    i = 0
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval = (min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1]))
        i += 1
    result.append(new_interval)
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    return result

