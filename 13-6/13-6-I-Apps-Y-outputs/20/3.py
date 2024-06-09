
def max_copies(s, k):
    n = len(s)
    if k > n:
        return []
    
    # count the frequency of each element in s
    count = {}
    for i in range(n):
        if s[i] not in count:
            count[s[i]] = 1
        else:
            count[s[i]] += 1
    
    # sort the elements of s in decreasing order of their frequency
    sorted_s = sorted(s, key=lambda x: count[x], reverse=True)
    
    # initialize the result array t with the first k elements of sorted_s
    t = sorted_s[:k]
    
    # iterate through the remaining elements of sorted_s
    for i in range(k, n):
        # if the current element is not in t, add it to t
        if sorted_s[i] not in t:
            t.append(sorted_s[i])
        # if the current element is already in t, remove the first occurrence of it from t
        else:
            t.remove(sorted_s[i])
            t.append(sorted_s[i])
    
    return t

