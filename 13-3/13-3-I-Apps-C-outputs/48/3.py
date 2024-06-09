
def count_coprime_pairs(a, b, c, d):
    count = 0
    for i in range(a, b+1):
        for j in range(c, d+1):
            if i == j:
                count += 1
            elif i % j == 0 or j % i == 0:
                continue
            else:
                count += 1
    return count

