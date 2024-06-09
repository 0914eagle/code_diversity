
def is_good_string(strings, s):
    for string in strings:
        if s.find(string) == -1:
            return False
    return True

def get_good_string(strings):
    min_len = float('inf')
    good_strings = []
    for string in strings:
        if len(string) < min_len:
            min_len = len(string)
        if is_good_string(strings, string):
            good_strings.append(string)

    if not good_strings:
        return "NO"

    good_strings.sort()
    return good_strings[0]

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

print(get_good_string(strings))

