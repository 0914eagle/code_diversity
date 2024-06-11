def unique_digits(x):
    
    # Your code here
    # unique_digits = []
    # for i in x:
    #     if not any(int(i) % 2 == 0 for i in str(i)):
    #         unique_digits.append(i)
    # return sorted(unique_digits)
    return sorted(i for i in x if not any(int(i) % 2 == 0 for i in str(i)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
