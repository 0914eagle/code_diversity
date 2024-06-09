
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
    
    # check if all substrings are different
    if len(freq) == n // 2 + 1:
        return s
    
    # if not, find the substring with the highest frequency and move it to the end of the string
    max_freq = max(freq.values())
    for substring in freq:
        if freq[substring] == max_freq:
            s = s.replace(substring, "")
            s += substring
            break
    
    return s

