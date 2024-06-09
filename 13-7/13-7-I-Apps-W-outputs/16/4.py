
def insert_interval(intervals, new_interval):
    
    # Check if the new interval is already present in the list
    if new_interval in intervals:
        return intervals
    
    # Initialize the result list
    result = []
    
    # Iterate through the intervals
    for interval in intervals:
        # Check if the new interval and the current interval overlap
        if interval[1] >= new_interval[0] and interval[0] <= new_interval[1]:
            # Merge the intervals
            new_interval[0] = min(interval[0], new_interval[0])
            new_interval[1] = max(interval[1], new_interval[1])
        else:
            # Add the current interval to the result list
            result.append(interval)
    
    # Add the new interval to the result list
    result.append(new_interval)
    
    # Return the updated list of intervals
    return result

