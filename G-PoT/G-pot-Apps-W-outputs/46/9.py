
n = int(input())
strings = [input() for _ in range(n)]

def is_good_string(s, substrings):
    for sub in substrings:
        if s.count(sub) < max(s.count(substring) for substring in substrings if substring != sub):
            return False
    return True

def get_all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

substrings = set()
for string in strings:
    substrings.update(get_all_substrings(string))

substrings = sorted(substrings, key=lambda x: (-len(x), x))

for sub in substrings:
    good_string = sub
    if is_good_string(good_string, strings):
        print(good_string)
        break
else:
    print("NO")
