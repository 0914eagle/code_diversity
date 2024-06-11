def intersection(interval1, interval2):
    
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"
    else:
        return "YES" if is_prime(abs(interval1[1] - interval2[0]) + 1) else "NO"


