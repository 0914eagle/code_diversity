def fizz_buzz(n: int):
    
    return sum(1 for i in range(1, n) if i % 11 == 0 or i % 13 == 0 and str(i).count('7'))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/exercises/ex010/solution.