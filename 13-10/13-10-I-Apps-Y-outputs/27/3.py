
def check_input(s):
    if len(s) != 4:
        return False
    for c in s:
        if not 'A' <= c <= 'Z':
            return False
    return True

def check_duplicate_characters(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True

def check_two_kinds_of_characters(s):
    seen = set()
    for c in s:
        if c in seen:
            seen.remove(c)
        else:
            seen.add(c)
    return len(seen) == 1

def solve(s):
    if not check_input(s):
        return "No"
    if not check_duplicate_characters(s):
        return "No"
    if not check_two_kinds_of_characters(s):
        return "No"
    return "Yes"

if __name__ == '__main__':
    s = input()
    print(solve(s))

