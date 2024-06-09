
def is_most_frequent(substring, strings):
    for s in strings:
        if s.count(substring) < strings.count(substring):
            return False
    return True

def find_good_string(strings):
    substrings = set()
    for s in strings:
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substrings.add(s[i:j])
    
    good_strings = []
    for substring in substrings:
        if is_most_frequent(substring, strings):
            good_strings.append(substring)
    
    if not good_strings:
        return "NO"
    
    min_length = min(len(s) for s in good_strings)
    min_length_strings = [s for s in good_strings if len(s) == min_length]
    
    return min(min_length_strings)

n = int(input())
strings = [input() for _ in range(n)]

result = find_good_string(strings)
print(result)
