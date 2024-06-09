
def get_trailing_zeroes(m):
    count = 0
    for i in range(1, m+1):
        if m % i == 0:
            count += 1
    return count

