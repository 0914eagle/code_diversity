
def get_maximum_cost(s, p):
    n = len(s)
    count = [0] * 2
    for i in range(n):
        if s[i] == "d":
            count[0] += 1
        else:
            count[1] += 1
    
    for i in range(p):
        if count[0] > count[1]:
            count[1] += 1
            count[0] -= 1
        else:
            count[0] += 1
            count[1] -= 1
    
    return max(count)

