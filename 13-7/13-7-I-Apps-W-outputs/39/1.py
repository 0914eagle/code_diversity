
def solve(s):
    n = len(s)
    if n == 1:
        return 0
    
    # count the number of distinct substrings
    distinct_substrings = set()
    for i in range(n):
        for j in range(i+1, n+1):
            distinct_substrings.add(s[i:j])
    
    # if there is only one distinct substring, then it's impossible to make all substrings distinct
    if len(distinct_substrings) == 1:
        return -1
    
    # count the minimum number of changes needed to make all substrings distinct
    changes = 0
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            if substring in distinct_substrings:
                continue
            else:
                changes += 1
                distinct_substrings.add(substring)
    
    return changes

