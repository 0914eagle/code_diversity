
def get_zeroes(m):
    count = 0
    for i in range(1, m+1):
        if str(factorial(i)).endswith(str(0) * m):
            count += 1
    return count

