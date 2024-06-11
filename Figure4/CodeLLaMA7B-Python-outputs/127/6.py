def intersection(interval1, interval2):
    
    if interval1[0] > interval1[1] or interval2[0] > interval2[1]:
        return "NO"
    elif interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"
    else:
        start = max(interval1[0], interval2[0])
        end = min(interval1[1], interval2[1])
        if start > end:
            return "NO"
        else:
            length = end - start + 1
            if length > 1:
                for i in range(2, length):
                    if length % i == 0:
                        return "NO"
                return "YES"
            else:
                return "NO"


if __name__ == "__main__":
    print(intersection((1, 2), (2, 3