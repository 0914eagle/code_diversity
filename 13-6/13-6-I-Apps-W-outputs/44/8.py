
def get_bonus_count(n):
    count = 0
    for i in range(2, n+1):
        if i % 2 == 0 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0 and i % 11 == 0:
            count += 1
    return count

