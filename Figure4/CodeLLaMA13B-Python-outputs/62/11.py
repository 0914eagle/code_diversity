def derivative(xs: list):
    
    return [i * j for i, j in enumerate(xs[1:], start=1) if j != 0]


if __