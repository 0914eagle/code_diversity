def count_nums(arr):
    
    return sum(1 for x in arr if sum(map(abs, map(int, str(x)))) > 0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
