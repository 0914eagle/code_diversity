
def is_good_string(string, strings):
    for s in strings:
        if string.count(s) < strings[0].count(s):
            return False
    return True

def get_good_string(strings):
    if len(strings) == 0:
        return "NO"
    min_len = len(strings[0])
    good_strings = []
    for string in strings:
        if len(string) == min_len and is_good_string(string, strings):
            good_strings.append(string)
        elif len(string) < min_len and is_good_string(string, strings):
            min_len = len(string)
            good_strings = [string]
    if len(good_strings) == 0:
        return "NO"
    return min(good_strings)

