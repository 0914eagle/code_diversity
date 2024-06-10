
def is_beautiful_sequence_possible(k, q):
    freq = {}
    for char in q:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    if any(count >= k for count in freq.values()):
        return False
    return True

def generate_beautiful_sequence(k, q):
    if not is_beautiful_sequence_possible(k, q):
        print("NO")
        return
    
    print("YES")
    freq = {}
    result = []
    for char in q:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
        result.append(char + str(freq[char]))
    
    for i in range(k - len(q)):
        result.append('a' + str(i))
    
    for string in result:
        print(string)

if __name__ == "__main__":
    k = int(input())
    q = input().strip()
    generate_beautiful_sequence(k, q)
