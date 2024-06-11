def sort_even(l: list):
    
    if len(l) == 0:
        return l
    else:
        return [l[0]] + sort_even(sorted([l[i] for i in range(len(l)) if i % 2 == 1]))


if __name__ == "__main__":
    import doctest