def intersection(interval1, interval2):
    

    # your code here
    if interval1[0] > interval1[1] or interval2[0] > interval2[1]:
        return "NO"
    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return "NO"
    if interval1[0] >= interval2[0] and interval1[1] <= interval2[1]:
        return "YES"
    if interval2[0] >= interval1[0] and interval2[1] <= interval1[1]:
        return "YES"
    if interval1[0] >= interval2[0] and interval2[1] <= interval1[1]:
        return "YES"
    if interval2[0] >= interval1[0] and interval1[1] <= interval2[1]:
        return "YES"
    return "NO"


print(intersection((1, 2), (2, 3)))
print(intersection((-1, 1), (0, 4)))
print(intersection((-3, -1), (-5, 5)))
