def intersection(interval1, interval2):
    
    # your code here
    if interval1[0] > interval2[0]:
        interval1, interval2 = interval2, interval1
    if interval1[1] < interval2[0]:
        return "NO"
    if interval1[1] == interval2[0]:
        return "NO"
    if interval1[1] > interval2[0] and interval1[1] < interval2[1]:
        return "NO"
    if interval1[1] == interval2[1]:
        return "NO"
    if interval1[1] > interval2[1]:
        return "NO"
    return "YES"


