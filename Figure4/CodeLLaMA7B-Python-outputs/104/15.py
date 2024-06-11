def unique_digits(x):
    
    # your code here
    result = []
    for i in x:
        if not any(int(j) % 2 == 0 for j in str(i)):
            result.append(i)
    return sorted(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
