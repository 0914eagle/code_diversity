def intersection(interval1, interval2):
    
    if interval1[0] <= interval2[0] and interval1[1] >= interval2[0]:
        return "YES" if is_prime(interval2[0] - interval1[0] + 1) else "NO"
    elif interval1[0] >= interval2[0] and interval1[0] <= interval2[1]:
        return "YES" if is_prime(interval1[1] - interval2[0] + 1) else "NO"
    else:
        return "NO"


