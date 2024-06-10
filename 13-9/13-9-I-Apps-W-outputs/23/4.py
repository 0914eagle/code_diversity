
def get_good_substrings(s):
    n = len(s)
    if n == 0:
        return []
    if s[0] == '0':
        return get_good_substrings(s[1:])
    substrings = []
    for i in range(1, n):
        if s[i] == '1':
            substrings.append(s[:i])
            break
    return substrings + get_good_substrings(s[i:])

def get_minimal_number_of_substrings(s):
    substrings = get_good_substrings(s)
    return len(substrings)

def get_substrings(s):
    substrings = get_good_substrings(s)
    return ' '.join(substrings)

if __name__ == '__main__':
    n = int(input())
    s = input()
    k = get_minimal_number_of_substrings(s)
    print(k)
    print(get_substrings(s))

