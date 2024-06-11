def intersection(interval1, interval2):
    
    if interval1[1] < interval2[0]:
        return "NO"
    if interval2[1] < interval1[0]:
        return "NO"
    if interval1[0] == interval2[0]:
        return "YES"
    if interval1[1] == interval2[1]:
        return "YES"
    if interval1[0] == interval2[1]:
        return "YES"
    if interval1[0] == interval2[0] and interval2[1] == interval1[1]:
        return "YES"
    if interval1[0] == interval2[1] and interval2[0] == interval1[1]:
        return "YES"
    if interval1[0] == interval2[0] and interval2[1] == interval1[0]:
        return "YES"
    if interval1[0] == interval2[1] and interval2[0] == interval1[0]:
        return "YES"
    if interval1[1] == interval2[0] and interval2[1] == interval1[1]:
        return "YES"
    if interval1[0] == interval2[0] and interval2[1] == interval1[0]:
        return "YES"
    if interval1[1] == interval2[1] and interval2[0] == interval1[1]:
        return "YES"
    if interval1[0] == interval2[1] and interval2[0] == interval1[0]:
        return "YES"
    if interval1[0] == interval2[0] and interval2[1] == interval1[1]:
        return "YES"
    if interval1[1] == interval2[1] and interval2[0] == interval1[0]:
        return "YES"
    if interval1[0] == interval2[1] and interval2[0] == interval1[1]:
        return "YES"
    if interval1[0] == interval2[0] and interval2[1] == interval1[0]:
        return "YES"
    if interval1[1] == interval2[1] and interval2[0] == interval1[1]:
        return "YES"
    if interval1[0] == interval2[0] and interval2[1] == interval1[1]:
        return "YES"
    if