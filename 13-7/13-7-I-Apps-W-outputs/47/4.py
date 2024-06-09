
def get_nearest_fraction(x, y, n):
    min_denom = float('inf')
    min_num = float('inf')
    for a in range(x+1):
        b = x*n//(a*y)
        if b <= n and abs(a-x*n//(y*b)) < min_num:
            min_num = abs(a-x*n//(y*b))
            min_denom = b
    return str(x*n//(y*min_denom))+'/'+str(min_denom)

