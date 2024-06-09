
def solve(n):
    if n > 180:
        return "impossible"
    
    scores = []
    for i in range(1, 21):
        if n - i >= 0:
            scores.append(i)
            n -= i
    
    if n == 0:
        return "\n".join([f"single {i}" for i in scores])
    
    for i in range(1, 21):
        if n - 2 * i >= 0:
            scores.append(2 * i)
            n -= 2 * i
    
    if n == 0:
        return "\n".join([f"double {i}" for i in scores])
    
    for i in range(1, 21):
        if n - 3 * i >= 0:
            scores.append(3 * i)
            n -= 3 * i
    
    if n == 0:
        return "\n".join([f"triple {i}" for i in scores])
    
    return "impossible"

