
def count_intervals(p, foe_pairs):
    n = len(p)
    intervals = []
    for i in range(n):
        for j in range(i+1, n):
            if not any(foe_pair in set(p[i:j+1]) for foe_pair in foe_pairs):
                intervals.append((i+1, j+1))
    return len(intervals)

