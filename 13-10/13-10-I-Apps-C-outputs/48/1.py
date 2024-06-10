
def get_unique_substrings(s, n):
    substrings = []
    for i in range(n//2):
        substring = s[i:i+n//2]
        if substring not in substrings:
            substrings.append(substring)
    return substrings

def rearrange_string(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    substrings = get_unique_substrings(s, n//2)
    if len(substrings) == n//2+1:
        return s
    else:
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    return "-1"
        return s

if __name__ == '__main__':
    s = input()
    print(rearrange_string(s))

