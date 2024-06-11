def fizz_buzz(n: int):
    
    return sum(int(str(i).count("7") and (i % 11 == 0 or i % 13 == 0)) for i in range(n))


if __name__ == "__main__":
    import doctest

    doctest