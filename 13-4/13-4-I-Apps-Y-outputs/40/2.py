
def count_triples(k, s):
    count = 0
    for x in range(k+1):
        for y in range(k+1):
            z = s - x - y
            if x + y + z == s and 0 <= x <= k and 0 <= y <= k and 0 <= z <= k:
                count += 1
    return count

