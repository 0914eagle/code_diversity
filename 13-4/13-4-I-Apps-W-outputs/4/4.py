
def get_pyramid_count(n):
    count = 0
    while n > 0:
        count += 1
        n -= count
    return count

