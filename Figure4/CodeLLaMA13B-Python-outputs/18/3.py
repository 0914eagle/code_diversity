def how_many_times(string: str, substring: str) -> int:
    
    return string.count(substring, 0, len(string))


if __name__ == '__main__':
    print(how_many_times('', 'a'))
    print(how_many_times('aaa', 'a