def make_a_pile(n):
    
    # your code here
    if n == 1:
        return [1]
    if n % 2 == 0:
        return [n] + make_a_pile(n - 2)
    else:
        return [n] + make_a_pile(n - 1)


if __name__ == "__main__":
    import doctest

    doctest.test