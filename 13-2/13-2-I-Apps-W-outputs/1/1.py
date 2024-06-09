
def get_bonus_count(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0:
            count += 1
    return count

