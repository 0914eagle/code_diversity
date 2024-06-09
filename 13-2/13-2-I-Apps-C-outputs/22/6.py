
def solve(n, k):
    if k < 1 or k > n:
        return "NO"
    
    MS = [i for i in range(1, n+1)]
    ME = [i for i in range(1, n+1)]
    VS = [i for i in range(1, n+1)]
    VE = [i for i in range(1, n+1)]
    
    for i in range(k):
        MS[i], ME[i] = i+1, i+2
        VS[i], VE[i] = i+1, i+2
    
    for i in range(k):
        for j in range(i+1, k):
            if MS[i] < MS[j] and ME[i] < ME[j]:
                return "NO"
            if VS[i] < VS[j] and VE[i] < VE[j]:
                return "NO"
    
    return "YES\n" + "\n".join([f"{MS[i]} {ME[i]}" for i in range(k)]) + "\n" + "\n".join([f"{VS[i]} {VE[i]}" for i in range(k)])

