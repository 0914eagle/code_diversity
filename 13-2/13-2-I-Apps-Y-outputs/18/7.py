
def get_max_prettiness(a):
    
    a.sort(reverse=True)
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return a[0] + a[1]
    if len(a) == 3:
        return max(a[0] + a[1], a[1] + a[2], a[0] + a[2])
    # If there are more than 3 problems, find the maximum possible prettiness by considering all possible combinations of 3 problems.
    max_prettiness = 0
    for i in range(len(a) - 2):
        for j in range(i + 1, len(a) - 1):
            for k in range(j + 1, len(a)):
                if a[i] % a[j] == 0 or a[i] % a[k] == 0 or a[j] % a[k] == 0:
                    continue
                prettiness = a[i] + a[j] + a[k]
                if prettiness > max_prettiness:
                    max_prettiness = prettiness
    return max_prettiness

