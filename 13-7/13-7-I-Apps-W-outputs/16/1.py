
def insert(intervals, new_interval):
    
    if not intervals:
        return [new_interval]
    
    # find the position where the new interval should be inserted
    left = 0
    right = len(intervals) - 1
    while left <= right:
        mid = (left + right) // 2
        if intervals[mid][0] < new_interval[0]:
            left = mid + 1
        elif intervals[mid][0] > new_interval[0]:
            right = mid - 1
        else:
            left = mid
            break
    
    # merge the new interval with the existing interval if necessary
    if left < len(intervals) and intervals[left][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[left][0])
        new_interval[1] = max(new_interval[1], intervals[left][1])
        intervals.pop(left)
        return insert(intervals, new_interval)
    
    # insert the new interval into the list
    intervals.insert(left, new_interval)
    return intervals

