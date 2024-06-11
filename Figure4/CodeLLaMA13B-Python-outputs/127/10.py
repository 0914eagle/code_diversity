def intersection(interval1, interval2):
    
    # your code here
    # print(interval1, interval2)
    if interval1[0] > interval2[0]:
        interval1, interval2 = interval2, interval1
    if interval1[1] < interval2[0]:
        return "NO"
    if interval1[1] >= interval2[1]:
        if interval1[1] - interval2[0] + 1 == 2:
            return "YES"
        else:
            return "NO"
    if interval1[1] - interval2[0] + 1 == 2:
        return "YES"
    else:
        return "NO"


print(intersection((1, 2), (2, 3)))
print(intersection((-1, 1), (0, 4)))
print(intersection((-3, -1), (-5, 5)))
print(intersection((-3, -1), (-1, 5)))
print(intersection((-3, -1), (-1, 1)))
print(intersection((-3, -1), (-1, 0)))
print(intersection((-3, -1), (-2, 0)))
print(intersection((-3, -1), (-2, 1)))
print(intersection((-3, -1), (-2, 2)))
print(intersection((-3, -1), (-2, 3)))
print(intersection((-3, -1), (-2, 4)))
print(intersection((-3, -1), (-2, 5)))
print(intersection((-3, -1), (-2, 6)))
print(intersection((-3, -1), (-2, 7)))
print(intersection((-3, -1), (-2, 8)))
print(intersection((-3, -1), (-2, 9)))
print(intersection((-3, -1), (-2, 10)))
print(intersection((-3, -1), (-2, 11)))
print(intersection((-3, -1), (-2, 12)))
print(intersection((-3, -1), (-2