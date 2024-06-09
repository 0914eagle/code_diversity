
def get_max_messiness(n, k):
    if n == 1:
        return 0
    
    pairs = [(i, i+1) for i in range(n-1)]
    max_messiness = 0
    
    for i in range(k):
        for pair in pairs:
            max_messiness += 1
            pairs.remove(pair)
            pairs.append((pair[1], pair[0]))
    
    return max_messiness

