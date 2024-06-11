def fizz_buzz(n: int):
    
    return sum(int(str(i).count("7") > 0) for i in range(n) if i % 11 == 0 or i % 13 == 0)


if __name__ == "__main__":
    import doctest

   