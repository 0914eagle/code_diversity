
def get_initial_sequences(a):
    n = len(a)
    if n == 0:
        return "NO"
    
    increasing = []
    decreasing = []
    for i in range(n):
        if a[i] > a[(i+1)%n]:
            increasing.append(a[i])
        elif a[i] < a[(i+1)%n]:
            decreasing.append(a[i])
    
    if len(increasing) == 0 and len(decreasing) == 0:
        return "NO"
    
    return "YES", len(increasing), increasing, len(decreasing), decreasing

