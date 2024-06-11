

def tri(n):
    
    if n == 0:
        return [1]
    elif n % 2 == 0:
        return [1, 3] + tri(n - 1)
    else:
        return [1] + tri(n - 1) + tri(n - 2) + tri(n + 1)


