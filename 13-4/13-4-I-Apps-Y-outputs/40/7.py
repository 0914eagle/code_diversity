
def get_triples(k, s):
    count = 0
    for x in range(k+1):
        for y in range(k+1):
            for z in range(k+1):
                if x + y + z == s:
                    count += 1
    return count

