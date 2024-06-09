
def get_max_rest(a):
    n = len(a)
    max_rest = 0
    curr_rest = 0
    for i in range(n):
        if a[i] == 0:
            curr_rest += 1
        else:
            max_rest = max(max_rest, curr_rest)
            curr_rest = 0
    return max(max_rest, curr_rest)

