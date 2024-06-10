
def is_duplicate_character(s):
    return len(set(s)) == 1

def is_duplicate_character_pair(s):
    return len(set(s)) == 2 and s.count(s[0]) == 2 and s.count(s[1]) == 2

def solve(s):
    if is_duplicate_character(s):
        return "No"
    if is_duplicate_character_pair(s):
        return "Yes"
    return "No"

if __name__ == '__main__':
    s = input()
    print(solve(s))

