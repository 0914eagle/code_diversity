
def solve(K, S):
    count = 0
    for x in range(K+1):
        for y in range(K+1):
            if x + y <= K:
                z = S - x - y
                if z >= 0 and z <= K:
                    count += 1
    return count

