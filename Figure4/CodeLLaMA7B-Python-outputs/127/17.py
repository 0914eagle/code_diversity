def intersection(interval1, interval2):
    
    if interval1[0] <= interval2[0] <= interval1[1]:
        return "YES"
    elif interval1[0] <= interval2[1] <= interval1[1]:
        return "YES"
    elif interval2[0] <= interval1[0] <= interval2[1]:
        return "YES"
    elif interval2[0] <= interval1[1] <= interval2[1]:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__