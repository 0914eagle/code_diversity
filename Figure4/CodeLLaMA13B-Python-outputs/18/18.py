def how_many_times(string: str, substring: str) -> int:
    
    if len(substring) == 0:
        return 0
    return (len(string) - len(string.replace(substring, '', 1))) // len(substring)


if __name__ == '__main__':
    print(how_