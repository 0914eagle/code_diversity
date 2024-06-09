
def f1(k):
    count = 0
    for i in range(1, k+1, 2):
        for j in range(2, k+1, 2):
            count += 1
    return count

