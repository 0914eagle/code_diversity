
def solve(s):
    vowels = set("aeiou")
    evens = set("02468")
    count = 0
    for i in range(len(s) - 1):
        if s[i] in vowels and s[i + 1] not in evens:
            count += 1
        elif s[i] not in vowels and s[i + 1] in evens:
            count += 1
    return count

