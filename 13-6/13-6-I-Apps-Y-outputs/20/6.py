
def solve(s, k):
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
    
    # sort the count in descending order
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    # create an empty array to store the result
    result = []
    
    # iterate through the count and add the elements to the result
    for i in range(k):
        result.append(count[i][0])
    
    return result

