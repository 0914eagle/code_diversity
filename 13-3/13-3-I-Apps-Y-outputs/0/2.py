
def count_shichi_go_san(n):
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    return count

