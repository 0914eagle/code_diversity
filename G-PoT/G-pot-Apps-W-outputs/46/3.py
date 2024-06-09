
def is_most_frequent(substring, strings):
    for s in strings:
        if substring not in s:
            return False
    max_count = max(s.count(substring) for s in strings)
    return all(s.count(substring) == max_count for s in strings)

n = int(input())
strings = [input() for _ in range(n)]

good_string = ""
for s in strings:
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            substring = s[j:j+i]
            if is_most_frequent(substring, strings):
                if not good_string or len(substring) < len(good_string) or (len(substring) == len(good_string) and substring < good_string):
                    good_string = substring

if good_string:
    print(good_string)
else:
    print("NO")
