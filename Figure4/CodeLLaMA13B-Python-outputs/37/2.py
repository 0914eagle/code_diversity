def sort_even(l: list):
    
    # Your code here
    even_sorted = sorted(l[::2])
    odd_sorted = l[1::2]
    return [even_sorted[i] + odd_sorted[i] for i in range(len(even_sorted))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
