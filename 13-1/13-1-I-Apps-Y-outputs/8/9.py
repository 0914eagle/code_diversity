
def get_maximum_copies(s, k):
    n = len(s)
    if k > n:
        return []
    
    # initialize a dictionary to store the frequency of each element in s
    freq = {}
    for i in range(n):
        if s[i] not in freq:
            freq[s[i]] = 1
        else:
            freq[s[i]] += 1
    
    # sort the dictionary by value in descending order
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # initialize an empty array to store the result
    result = []
    
    # iterate through the dictionary and add the k most frequent elements to the result
    for i in range(k):
        result.append(freq[i][0])
    
    return result

