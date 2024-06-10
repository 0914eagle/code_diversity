
import re

def how_many_times(string: str, substring: str) -> int:
    count = 0
    if not string or not substring:
        return count

    pattern = re.compile(f'(?={re.escape(substring)})')
    matches = pattern.finditer(string)
    for _ in matches:
        count += 1

    return count

if __name__ == "__main__":
    string, substring = input().strip().split()
    print(how_many_times(string, substring))
