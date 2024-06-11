def string_sequence(n: int) -> str:
    
    return ' '.join(str(i) for i in range(n + 1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
