
def count_occurrences(s, t, l, r):
    count = 0
    for i in range(l, r + 1):
        if s[i:i+len(t)] == t:
            count += 1
    return count

