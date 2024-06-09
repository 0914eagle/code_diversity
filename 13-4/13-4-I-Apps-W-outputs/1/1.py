
def is_good_string(s, strings):
    for string in strings:
        if s not in string:
            return False
    return True

def get_good_string(strings):
    min_len = float('inf')
    good_strings = []
    for string in strings:
        if len(string) < min_len:
            min_len = len(string)
        if is_good_string(string, strings):
            good_strings.append(string)
    if not good_strings:
        return "NO"
    return min(good_strings)

n = int(input())
strings = []
for i in range(n):
    strings.append(input())
print(get_good_string(strings))

