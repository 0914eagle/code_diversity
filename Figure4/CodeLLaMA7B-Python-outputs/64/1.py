FIX = 

def vowels_count(s):
    
    return sum(s.count(c) for c in "aeiouy")


if __name__ == "__main__":
    import doctest
    doctest.testmod