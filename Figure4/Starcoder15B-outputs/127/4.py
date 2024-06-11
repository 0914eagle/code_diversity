def intersection(interval1, interval2):
    
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"
    else:
        return "YES" if is_prime(min(interval1[1], interval2[1]) - max(interval1[0], interval2[0]) + 1) else "NO"


