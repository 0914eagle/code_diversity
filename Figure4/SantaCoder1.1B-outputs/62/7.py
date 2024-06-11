def derivative(xs: list):
    
    if len(xs) == 0:
        return []
    if len(xs) == 1:
        return [xs[0]]
    return [xs[i] + xs[i + 1] * xs[i] for i in range(len(xs) - 1)]


