
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
    
    # check if all substrings are different
    if len(freq) == n // 2 + 1:
        return s
    
    # if not, find a permutation of the letters that produces all different substrings
    permutation = []
    for i in range(n // 2):
        for j in range(n // 2):
            if s[i + j] not in permutation:
                permutation.append(s[i + j])
                break
    
    return "".join(permutation)

