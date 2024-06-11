def intersection(interval1, interval2):
    

    # Your code here
    # print(interval1, interval2)
    # print(interval1[0], interval1[1])
    # print(interval2[0], interval2[1])

    # if interval1[0] > interval1[1]:
    #     return "NO"
    # if interval2[0] > interval2[1]:
    #     return "NO"

    # if interval1[0] > interval2[0] and interval1[0] > interval2[1]:
    #     return "NO"
    # if interval1[1] < interval2[0] and interval1[1] < interval2[1]:
    #     return "NO"

    # if interval1[0] <= interval2[0] and interval1[1] >= interval2[0]:
    #     return "YES"
    # if interval1[0] <= interval2[1] and interval1[1] >= interval2[1]:
    #     return "YES"

    # if interval2[0] <= interval1[0] and interval2[1] >= interval1[0]:
    #     return "YES"
    # if interval2[0] <= interval1[1] and interval2[1] >= interval1[1]:
    #     return "YES"

    # return "NO"

    # return "YES" if interval1[0] <= interval2[0] <= interval1[1] <= interval2[1] else "NO"

    return "YES" if interval1[0] <= interval2[0] <= interval1[1] <= interval2[1] else "NO"


print(intersection((1, 2), (2, 3)))
print(intersection((-1, 1), (0, 4)))
print(intersection((-3, -1), (-5, 5)))
