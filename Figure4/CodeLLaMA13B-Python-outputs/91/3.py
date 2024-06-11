def is_bored(S):
    
    count = 0
    for i in S.split("."):
        if i.strip().startswith("I"):
            count += 1
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
