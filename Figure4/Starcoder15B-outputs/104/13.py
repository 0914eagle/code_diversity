def unique_digits(x):
    
    return [i for i in x if not any(int(j) % 2 == 0 for j in str(i))]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/week05/0