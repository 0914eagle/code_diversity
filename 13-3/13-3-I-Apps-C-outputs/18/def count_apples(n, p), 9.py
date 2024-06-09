
def count_apples(n, p):
    apples = 1
    for i in range(2, n+1):
        if p[i-2] == 1:
            apples += 1
        else:
            apples -= 1
    return apples

