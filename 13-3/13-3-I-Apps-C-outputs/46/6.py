
def solve(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    # create a dictionary to store the frequencies of each substring
    freq = {}
    for i in range(n // 2):
        substring = s[i:i + n // 2]
        if substring not in freq:
            freq[substring] = 1
        else:
            freq[substring] += 1
    
    # check if there are any duplicates
    for substring in freq:
        if freq[substring] > 1:
            return "-1"
    
    # if all substrings are unique, return the original string
    return s

