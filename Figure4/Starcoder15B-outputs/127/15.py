def intersection(interval1, interval2):
    
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"
    else:
        if interval1[0] < interval2[0]:
            start = interval2[0]
        else:
            start = interval1[0]
        if interval1[1] > interval2[1]:
            end = interval2[1]
        else:
            end = interval1[1]
        if is_prime(end - start):
            return "YES"
        else:
            return "NO"


