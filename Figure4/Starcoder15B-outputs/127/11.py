def intersection(interval1, interval2):
    
    start1, end1 = interval1
    start2, end2 = interval2
    if start1 > end2 or start2 > end1:
        return "NO"
    if start1 <= start2 <= end1 <= end2:
        return "YES" if is_prime(end1 - start2 + 1) else "NO"
    if start2 <= start1 <= end2 <= end1:
        return "YES" if is_prime(end2 - start1 + 1) else "NO"
    if start1 <= start2 <= end2 <= end1:
        return "YES" if is_prime(end2 - start2 + 1) else "NO"
    if start2 <= start1 <= end1 <= end2:
        return "YES" if is_prime(end1 - start1 + 1) else "NO"


