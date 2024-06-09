
def get_max_cuts(s, k):
    n = len(s)
    if k > n:
        return []
    
    # count the frequency of each element in s
    count = [0] * (n + 1)
    for i in range(n):
        count[s[i]] += 1
    
    # sort the elements in decreasing order of their frequency
    sorted_s = sorted(s, key=lambda x: count[x], reverse=True)
    
    # create a hash map to store the indices of the elements in sorted_s
    ind = {sorted_s[i]: i for i in range(n)}
    
    # initialize the result array t with the first k elements of sorted_s
    t = sorted_s[:k]
    
    # iterate through the remaining elements of sorted_s
    for i in range(k, n):
        # if the current element is not in t, add it to t
        if ind[sorted_s[i]] > ind[t[-1]]:
            t.append(sorted_s[i])
    
    return t

