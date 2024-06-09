
def get_available_dishes(m, k, a, t_j, r_j):
    available_dishes = []
    for i in range(k):
        if a[i] > 0:
            available_dishes.append(i)
    
    for i in range(m - 1):
        if t_j[i] > 0 and r_j[i] == 1:
            available_dishes.remove(t_j[i] - 1)
    
    return available_dishes

