def derivative(xs: list):
    
    return [x * (xs[i + 1] - xs[i]) for i, x in enumerate(xs[:-1])]


