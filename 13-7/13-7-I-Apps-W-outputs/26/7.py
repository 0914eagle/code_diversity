
def get_num_x(a, m):
    count = 0
    for x in range(m):
        if __gcd(a, m) == __gcd(a + x, m):
            count += 1
    return count

