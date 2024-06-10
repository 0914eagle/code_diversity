
def is_beautiful_sequence_possible(k, q):
    freq = {}
    for char in q:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    if any(freq[char] >= k for char in freq):
        return "NO"
    
    result = []
    for char in sorted(freq.keys()):
        result.append(char * min(k, freq[char]))
        k -= min(k, freq[char])
    
    return "YES", result

if __name__ == "__main__":
    k = int(input())
    q = input().strip()
    
    result = is_beautiful_sequence_possible(k, q)
    if result == "NO":
        print("NO")
    else:
        print(result[0])
        for s in result[1]:
            print(s)
