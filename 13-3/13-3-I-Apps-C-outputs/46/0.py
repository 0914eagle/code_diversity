
def solve(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    # create a dictionary to store the frequency of each substring
    freq = {}
    for i in range(n // 2):
        substring = s[i:i + n // 2]
        if substring not in freq:
            freq[substring] = 1
        else:
            freq[substring] += 1
    
    # if there is a substring that appears more than once, it is not possible to rearrange the string
    for value in freq.values():
        if value > 1:
            return "-1"
    
    # if all substrings are different, return the original string
    return s

