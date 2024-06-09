
def is_good_string(s, strings):
    for string in strings:
        if string not in s:
            return False
    return True

def get_good_string(strings):
    min_len = float('inf')
    good_strings = []
    for string in strings:
        if len(string) < min_len:
            min_len = len(string)
            good_strings = [string]
        elif len(string) == min_len:
            good_strings.append(string)
    
    if len(good_strings) == 0:
        return "NO"
    
    return min(good_strings)

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

print(get_good_string(strings))

