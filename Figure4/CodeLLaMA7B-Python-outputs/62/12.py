def derivative(xs: list):
    
    return [xs[i] * i for i in range(1, len(xs))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
