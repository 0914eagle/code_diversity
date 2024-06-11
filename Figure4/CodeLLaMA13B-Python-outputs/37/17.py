def sort_even(l: list):
    
    even_list = []
    for i in range(0, len(l), 2):
        even_list.append(l[i])
    even_list.sort()
    for i in range(0, len(l), 2):
        l[i] = even_list[i // 2]
    return l


if __name__ == "__main__":
    import doctest

    doctest.testmod()
