
def count_pairs(n, jaap, jan, thijs):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if jaap[i] == jan[i] == thijs[i] == jaap[j] == jan[j] == thijs[j]:
                count += 1
    return count

