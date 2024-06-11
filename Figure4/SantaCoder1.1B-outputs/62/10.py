def derivative(xs: list):
    
    if len(xs) == 1:
        return [1]
    else:
        return [xs[1] * xs[0] + xs[2] * xs[0]**2 + xs[3] * xs[0]**3 + xs[4] * xs[0]**4 + xs[5] * xs[0]**5]


