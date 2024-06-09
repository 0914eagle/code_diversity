
def number_of_ways_to_distribute_candies(n):
    count = 0
    for a in range(1, n//2+1):
        b = n - a
        if a > b and a % 1 == 0 and b % 1 == 0:
            count += 1
    return count

