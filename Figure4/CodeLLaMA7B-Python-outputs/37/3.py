def sort_even(l: list):
    
    # Your code here
    even = []
    for i in range(len(l)):
        if i % 2 == 0:
            even.append(l[i])
    even.sort()
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = even[i // 2]
    return l


if __name__ == "__main__":
    import doctest

    doctest.testmod()
