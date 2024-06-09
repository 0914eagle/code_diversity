
def get_maximum_copies(s, k):
    n = len(s)
    if k > n:
        return []
    
    # count the frequency of each element in s
    count = [0] * (n + 1)
    for i in range(n):
        count[s[i]] += 1
    
    # sort the array s in non-decreasing order
    s.sort()
    
    # initialize the result array t with the first k elements of s
    t = s[:k]
    
    # iterate through the remaining elements of s
    for i in range(k, n):
        # if the current element is not in t, add it to t
        if s[i] not in t:
            t.append(s[i])
        # if the current element is already in t, remove the first occurrence of it
        else:
            t.remove(s[i])
            t.append(s[i])
    
    return t

