
def get_substrings(s, n):
    substrings = []
    for i in range(len(s) - n + 1):
        substrings.append(s[i:i+n])
    return substrings

def rearrange(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    substrings = get_substrings(s, n//2)
    seen = set()
    for substring in substrings:
        if substring in seen:
            return "-1"
        seen.add(substring)
    
    permutations = itertools.permutations(s)
    for permutation in permutations:
        substrings = get_substrings(permutation, n//2)
        if all(substring not in seen for substring in substrings):
            return "".join(permutation)
    
    return "-1"

if __name__ == '__main__':
    s = input()
    print(rearrange(s))

