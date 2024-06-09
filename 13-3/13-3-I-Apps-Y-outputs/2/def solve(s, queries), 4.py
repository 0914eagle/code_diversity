
def solve(s, queries):
    # Initialize a dictionary to store the count of AC as a substring
    ac_count = {}
    
    # Iterate through the string and increment the count of AC as a substring
    for i in range(len(s) - 1):
        if s[i:i+2] == "AC":
            ac_count[i] = ac_count.get(i, 0) + 1
    
    # Iterate through the queries and return the count of AC as a substring for each query
    result = []
    for l, r in queries:
        count = 0
        for i in range(l, r+1):
            count += ac_count.get(i, 0)
        result.append(count)
    return result

