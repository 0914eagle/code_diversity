def sort_third(l: list):
    
    l_prime = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime.append(sorted(l[i::3]))
        else:
            l_prime.append(l[i])
    return [item for sublist in l_prime for item in sublist]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
