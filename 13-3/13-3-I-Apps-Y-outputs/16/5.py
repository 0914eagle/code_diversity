
def max_rest(n, a):
    max_rest = 0
    current_rest = 0
    for i in range(n):
        if a[i] == 0:
            current_rest += 1
        else:
            max_rest = max(max_rest, current_rest)
            current_rest = 0
    
    max_rest = max(max_rest, current_rest)
    return max_rest

