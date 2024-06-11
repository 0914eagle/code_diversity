def monotonic(l: list):
    
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(
        l[i] >= l[i + 1] for i in range(len(l) - 1)
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
