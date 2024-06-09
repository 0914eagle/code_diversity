
def get_max_cuts(s, k):
    n = len(s)
    if k > n:
        return []
    
    # count the frequency of each element in s
    count = [0] * (n + 1)
    for i in range(n):
        count[s[i]] += 1
    
    # sort the elements in descending order of their frequency
    sorted_s = sorted(s, key=lambda x: count[x], reverse=True)
    
    # find the k elements with the highest frequency that can be used to form the array t
    t = sorted_s[:k]
    
    # count the number of copies of t that can be cut out of s
    num_cuts = 0
    for i in range(n - k + 1):
        if s[i:i+k] == t:
            num_cuts += 1
    
    return t

