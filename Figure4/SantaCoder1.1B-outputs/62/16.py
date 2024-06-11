def derivative(xs: list):
    
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return [xs[0]]
    if len(xs) == 2:
        return [xs[0]] + [xs[1] * x for x in xs[0:1]]
    return [xs[0]] + [xs[1] * x + xs[2] * x**2 for x in xs[0:1]] + [xs[1] * x**2 + xs[2] * x**3 for x in xs[0:1]]


