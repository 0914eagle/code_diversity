def derivative(xs: list):
    
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return [xs[0]]
    return [xs[0]] + [x * xs[i] for i, x in enumerate(xs[1:])]


