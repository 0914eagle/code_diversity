
def count_coprime_pairs(a, b, c, d):
    count = 0
    for x in range(a, b+1):
        for y in range(c, d+1):
            if is_coprime(x, y):
                count += 1
    return count

def is_coprime(x, y):
    return len(set(range(2, min(x, y)+1)).intersection(set(range(2, min(x, y)+1)))) == 0

