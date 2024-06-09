
def insert_interval(intervals, new_interval):
    
    result = []
    inserted = False
    for interval in intervals:
        if not inserted and new_interval[0] > interval[1]:
            result.append(interval)
        elif not inserted and new_interval[0] <= interval[1]:
            result.append([min(interval[0], new_interval[0]), max(interval[1], new_interval[1])])
            inserted = True
        elif inserted and new_interval[0] > interval[1]:
            result.append([min(interval[0], new_interval[0]), max(interval[1], new_interval[1])])
        else:
            result.append(interval)
    if not inserted:
        result.append(new_interval)
    return result

