
def is_good_string(string, substrings):
    for substring in substrings:
        if string.count(substring) < substrings[substring]:
            return False
    return True

def get_good_string(substrings):
    min_len = float('inf')
    good_string = ""
    for string in substrings:
        if len(string) < min_len and is_good_string(string, substrings):
            min_len = len(string)
            good_string = string
    if good_string == "":
        return "NO"
    return good_string

n = int(input())
substrings = {}
for i in range(n):
    string = input()
    for j in range(len(string)):
        substring = string[j:]
        if substring not in substrings:
            substrings[substring] = 0
        substrings[substring] += 1

print(get_good_string(substrings))

