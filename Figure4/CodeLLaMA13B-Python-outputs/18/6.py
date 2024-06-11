def how_many_times(string: str, substring: str) -> int:
    
    return string.count(substring)


if __name__ == '__main__':
    print(how_many_times('', 'a'))
    print(how_many_times('aaa', 'a'))
    print(how_many_