
def find_multiple(k):
    count = 1
    while True:
        if count % k == 0:
            return count
        count = count * 10 + 7
    return -1

