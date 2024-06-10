
import re

def how_many_times(string: str, substring: str) -> int:
    count = 0
    if not string or not substring:
        return count
    
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    
    return count

if __name__ == "__main__":
    string, substring = input().strip().split()
    print(how_many_times(string, substring))
