
def is_most_frequent(substring, strings):
    max_count = 0
    for s in strings:
        count = s.count(substring)
        if count > max_count:
            max_count = count
    return all(s.count(substring) == max_count for s in strings)

def find_good_string(strings):
    substrings = set()
    for s in strings:
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substrings.add(s[i:j])
    
    substrings = sorted(list(substrings), key=lambda x: (-len(x), x))
    
    for substring in substrings:
        if is_most_frequent(substring, strings):
            return substring
    return "NO"

n = int(input())
strings = [input() for _ in range(n)]

result = find_good_string(strings)
print(result)
