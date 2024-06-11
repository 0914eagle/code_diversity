def intersection(interval1, interval2):
    
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 > end2:
        return "NO"
    if start2 > end1:
        return "NO"
    if start1 == end1 and start2 == end2:
        return "YES"
    if start1 == end1 or start2 == end2:
        return "NO"
    if start1 < end2 and start2 < end1:
        return "YES"
    return "NO"


