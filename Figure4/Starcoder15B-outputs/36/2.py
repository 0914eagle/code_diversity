def fizz_buzz(n: int):
    
    return sum(str(i).count('7') for i in range(1, n) if i % 11 == 0 or i % 13 == 0)


if __name__ == '__main__':
    import