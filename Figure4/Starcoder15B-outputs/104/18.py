def unique_digits(x):
    
    # Your code here
    return [x for x in x if not any(int(y) % 2 == 0 for y in str(x))]

if __name__ == '__main__':
    import doctest
    doctest.test