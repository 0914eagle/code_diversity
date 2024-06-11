def derivative(xs: list):
    
    return [x + xs[i] * x**i for i, x in enumerate(xs)]


