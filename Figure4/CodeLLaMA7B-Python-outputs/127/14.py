def intersection(interval1, interval2):
    
    if interval1[0] > interval1[1] or interval2[0] > interval2[1]:
        return "NO"
    elif interval1[0] <= interval2[0] <= interval1[1]:
        if interval2[0] <= interval1[1]:
            return "YES" if len(set(range(interval2[0], interval1[1] + 1))) == 1 else "NO"
        else:
            return "YES" if len(set(range(interval1[0], interval2[1] + 1))) == 1 else "NO"
    elif interval2[0] <= interval1[0] <= interval2[1]:
        if interval1[0] <= interval2[1]:
            return "YES" if len(set(range(interval1[0], interval2[1] + 1))) == 1 else "NO"
        else:
            return "YES" if len(set(range(interval2[0], interval1[1] + 1))) == 1 else "NO"
    else:
        return "NO"


if