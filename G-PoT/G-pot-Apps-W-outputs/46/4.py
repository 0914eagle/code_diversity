
def is_most_frequent(substring, strings):
    count = 0
    for s in strings:
        count += s.count(substring)
    for s in strings:
        if s.count(substring) > count:
            return False
    return True

def find_good_string(strings):
    substrings = set()
    for s in strings:
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substrings.add(s[i:j])
    
    good_strings = []
    for s in substrings:
        if is_most_frequent(s, strings):
            good_strings.append(s)
    
    if not good_strings:
        return "NO"
    
    good_strings.sort(key=lambda x: (len(x), x))
    return good_strings[0]

n = int(input())
strings = [input() for _ in range(n)]

result = find_good_string(strings)
print(result)
