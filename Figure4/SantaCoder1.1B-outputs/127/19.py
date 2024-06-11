def intersection(interval1, interval2):
    
    start1, end1 = interval1
    start2, end2 = interval2
    if end1 < start2 or end2 < start1:
        return "NO"
    if end1 == start2 and end2 == start1:
        return "YES"
    if end1 == start2 or end2 == start1:
        return "NO"
    if end1 > start2 and end2 > start1:
        return "YES"
    if end1 > start2 or end2 > start1:
        return "NO"


if __name__ == '__main__':
    print(intersection((1, 2), (2, 3)))
    print(intersection((-1, 1), (0, 4)))
    print(intersection((-3, -1), (-5, 5)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4), (3, 5)))
    print(intersection((1, 3), (2, 4), (3, 5), (4, 6)))
    print(intersection((1,