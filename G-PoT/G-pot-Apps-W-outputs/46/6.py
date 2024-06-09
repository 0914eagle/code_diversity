
def is_most_frequent(substring, strings):
    for s in strings:
        if substring not in s:
            return False
    count_substring = sum(1 for i in range(len(s)) if s[i:i+len(substring)] == substring)
    for s in strings:
        if sum(1 for i in range(len(s)) if s[i:i+len(substring)] == substring) < count_substring:
            return False
    return True

n = int(input())
strings = [input() for _ in range(n)]

good_string = ""
for s in strings:
    for i in range(1, len(s)+1):
        substring = s[:i]
        if is_most_frequent(substring, strings):
            if not good_string or len(substring) < len(good_string) or (len(substring) == len(good_string) and substring < good_string):
                good_string = substring

if good_string:
    print(good_string)
else:
    print("NO")
