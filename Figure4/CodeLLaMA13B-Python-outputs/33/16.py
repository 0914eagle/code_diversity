def sort_third(l: list):
    
    # Your code here
    l_copy = l.copy()
    for i in range(0, len(l), 3):
        l_copy[i:i+3] = sorted(l[i:i+3])
    return l_copy


if __name__ == "__main__":
    import doctest