
def get_number_of_integers(a, m):
    count = 0
    for x in range(m):
        if a % x == 0 and m % (a + x) == 0:
            count += 1
    return count

