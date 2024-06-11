def intersection(interval1, interval2):
    
    if interval1[0] <= interval2[0] and interval1[1] >= interval2[0]:
        if interval1[1] <= interval2[1]:
            return "YES"
        else:
            return "NO"
    elif interval1[0] >= interval2[0] and interval1[0] <= interval2[1]:
        if interval1[1] <= interval2[1]:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    print(intersection((1, 2), (2, 3)))
    print(intersection((-1, 1), (0, 4)))
    print(intersection((-3, -1), (-5, 5)))
