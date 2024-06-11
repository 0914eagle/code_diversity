def unique_digits(x):
    
    # Your code here
    # return [x for x in x if not any(d%2==0 for d in str(x))]
    return [x for x in x if not any(d%2==0 for d in str(x))]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
