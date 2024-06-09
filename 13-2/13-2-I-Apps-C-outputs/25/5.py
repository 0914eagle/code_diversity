
def get_total_segments(n, k, a):
    total = 0
    for i in range(n):
        for j in range(i, n):
            segment_sum = sum(a[i:j+1])
            if segment_sum >= 0 and segment_sum ** (1/k) % 1 == 0:
                total += 1
    return total

