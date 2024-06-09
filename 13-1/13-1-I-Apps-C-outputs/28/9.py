
def solve(s):
    count = 0
    for i in range(len(s)):
        if s[i].isupper():
            if s[i].lower() + s[i+1:].lower() == "bulbasaur":
                count += 1
                s = s[:i] + s[i+1:]
    return count

