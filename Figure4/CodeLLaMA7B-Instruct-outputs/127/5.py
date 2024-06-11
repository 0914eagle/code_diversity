

def intersection(interval1, interval2):
    

    # Check if the intervals intersect
    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return "NO"

    # Calculate the intersection
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    length = end - start + 1

    # Check if the length is a prime number
    if length <= 1:
        return "NO"
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return "NO"
    return "YES"


