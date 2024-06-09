
def min_f(a):
    n = len(a)
    min_val = float('inf')
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                val = (i-j)**2 + (sum(a[min(i,j):max(i,j)+1]))**2
                if val < min_val:
                    min_val = val
    return min_val

