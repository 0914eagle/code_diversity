def derivative(xs: list):
    
    return [i * j for i, j in zip(range(1, len(xs)), xs[1:])]


if __