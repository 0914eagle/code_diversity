def intersection(interval1, interval2):
    
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"
    if interval1[0] == interval2[0]:
        return "YES"
    if interval1[1] == interval2[1]:
        return "YES"
    if interval1[0] == interval2[1]:
        return "YES"
    if interval1[0] < interval2[0] or interval2[0] < interval1[1]:
        return "NO"
    if interval1[1] < interval2[0] or interval2[1] < interval1[1]:
        return "NO"
    if interval1[0] == interval2[1]:
        return "YES"
    if interval1[1] == interval2[0]:
        return "YES"
    if interval1[0] < interval2[1] or interval2[1] < interval1[0]:
        return "NO"
    if interval1[1] < interval2[1] or interval2[1] < interval1[0]:
        return "NO"
    return "YES"


if __name__ == '__main__':
    print(intersection((1, 2), (2, 3)))
    print(intersection((-1, 1), (0, 4)))
    print(intersection((-3, -1), (-5, 5)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
    print(intersection((1, 3), (2, 4)))
   