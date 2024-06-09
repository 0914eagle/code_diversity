
def count_intervals(p, foe_pairs):
    n = len(p)
    intervals = []
    for i in range(n):
        for j in range(i+1, n):
            interval = (p[i], p[j])
            if not any(interval[0] <= a <= interval[1] or interval[0] <= b <= interval[1] for a, b in foe_pairs):
                intervals.append(interval)
    return len(set(intervals))

