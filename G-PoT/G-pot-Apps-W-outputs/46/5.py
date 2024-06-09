
n = int(input())
strings = [input() for _ in range(n)]

def is_good_string(s, substrings):
    for sub in substrings:
        if s.count(sub) < max(s.count(subs) for subs in substrings if subs != sub):
            return False
    return True

def generate_substrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.add(s[i:j])
    return substrings

substrings = set()
for string in strings:
    substrings |= generate_substrings(string)

good_strings = []
for sub in substrings:
    s = sub
    for string in strings:
        if string.count(sub) < s.count(sub):
            s = string
    if is_good_string(s, substrings):
        good_strings.append(s)

if good_strings:
    print(min(good_strings, key=lambda x: (len(x), x)))
else:
    print("NO")
