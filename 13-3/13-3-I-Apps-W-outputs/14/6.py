
def get_available_dishes(m, k, a, t, r):
    available_dishes = []
    for i in range(k):
        if a[i] > 0:
            available_dishes.append(i)
    
    for i in range(m - 1):
        if t[i] != 0 and r[i] == 1:
            available_dishes.remove(t[i] - 1)
    
    return available_dishes

