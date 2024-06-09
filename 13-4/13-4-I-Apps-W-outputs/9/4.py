
def count_ways(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    if n == 5:
        return 7
    if n == 6:
        return 13
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3) + count_ways(n-4)

