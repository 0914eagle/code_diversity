def unique_digits(x):
    
    return sorted(filter(lambda x: not any(d%2 == 0 for d in str(x)), x))


if __name__ == "__main__":
    import doctest
