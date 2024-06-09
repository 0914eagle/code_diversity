
def insert_interval(intervals, new_interval):
    
    result = []
    inserted = False
    for interval in intervals:
        # if the current interval has ended before the new interval starts, keep it in the result
        if interval[1] < new_interval[0]:
            result.append(interval)
        # if the new interval ends before the current interval starts, keep the new interval in the result
        elif new_interval[1] < interval[0]:
            result.append(new_interval)
            inserted = True
            new_interval = None
        # if the new interval overlaps with the current interval, merge them
        else:
            result.append([min(interval[0], new_interval[0]), max(interval[1], new_interval[1])])
            inserted = True
            new_interval = None
    # if the new interval was not inserted, add it to the result
    if not inserted:
        result.append(new_interval)
    return result

