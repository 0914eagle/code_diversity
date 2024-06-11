def sort_even(l: list):
    
    # Your code here
    even_sorted = []
    odd_sorted = []
    for i in range(len(l)):
        if i % 2 == 0:
            even_sorted.append(l[i])
        else:
            odd_sorted.append(l[i])
    even_sorted.sort()
    return odd_sorted + even_sorted


if __name__ == "__main__":
    import doctest

    doct