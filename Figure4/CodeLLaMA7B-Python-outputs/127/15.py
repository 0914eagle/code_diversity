def intersection(interval1, interval2):
    
    if interval1[0] <= interval2[0] and interval1[1] >= interval2[0]:
        start = interval2[0]
    elif interval1[0] >= interval2[0] and interval1[0] <= interval2[1]:
        start = interval1[0]
    else:
        return "NO"

    if interval1[1] >= interval2[1] and interval1[1] <= interval2[0]:
        end = interval2[1]
    elif interval1[1] <= interval2[1] and interval1[1] >= interval2[0]:
        end = interval1[1]
    else:
        return "NO"

    if start <= end:
        length = end - start + 1
        if length > 1:
            for i in range(2, length):
                if length % i == 0:
                    return "NO"
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == "__main__":
    print(