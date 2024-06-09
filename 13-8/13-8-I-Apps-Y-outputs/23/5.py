
def get_sequences(a):
    n = len(a)
    if n == 0:
        return "NO"
    
    increasing = []
    decreasing = []
    for i in range(n):
        if a[i] not in increasing and a[i] not in decreasing:
            increasing.append(a[i])
        elif a[i] in increasing:
            increasing.remove(a[i])
            increasing.append(a[i])
        elif a[i] in decreasing:
            decreasing.remove(a[i])
            decreasing.append(a[i])
    
    increasing = sorted(increasing)
    decreasing = sorted(decreasing, reverse=True)
    
    if len(increasing) + len(decreasing) != n:
        return "NO"
    
    return "YES", len(increasing), increasing, len(decreasing), decreasing

