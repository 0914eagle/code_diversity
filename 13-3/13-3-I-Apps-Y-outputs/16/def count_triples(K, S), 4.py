
def count_triples(K, S):
    count = 0
    for x in range(K+1):
        for y in range(K+1-x):
            z = S - x - y
            if x + y + z == S and 0 <= x <= K and 0 <= y <= K and 0 <= z <= K:
                count += 1
    return count

