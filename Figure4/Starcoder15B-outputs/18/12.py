def how_many_times(string: str, substring: str) -> int:
    
    if not string or not substring:
        return 0
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            count += 1
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/tests/test_how_many_times.py
from unittest import TestCase
