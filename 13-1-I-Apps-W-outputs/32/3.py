
def count_intervals(p, foe_pairs):
    n = len(p)
    intervals = []
    for i in range(n):
        for j in range(i+1, n):
            interval = (p[i], p[j])
            if not any(foe_pair in interval for foe_pair in foe_pairs):
                intervals.append(interval)
    return len(set(intervals))

