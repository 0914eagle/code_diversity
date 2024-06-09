
def stick_cutting(n):
    count = 0
    for i in range(1, int(n/2)+1):
        for j in range(i+1, int(n/2)+1):
            if i + j == n:
                count += 1
    return count

