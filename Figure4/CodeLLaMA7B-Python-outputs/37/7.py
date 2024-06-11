def sort_even(l: list):
    
    # Your code here
    even = [l[i] for i in range(0, len(l), 2)]
    even.sort()
    return [even[i // 2] if i % 2 == 0 else l[i] for i in range(len(l))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
