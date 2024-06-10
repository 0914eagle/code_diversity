
def is_beautiful_sequence_possible(k, q):
    freq = {}
    for char in q:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    if any(freq[char] >= k for char in freq):
        return "YES"
    else:
        return "NO"

def generate_beautiful_sequence(k, q):
    freq = {}
    result = []
    for char in q:
        if char not in freq:
            freq[char] = 1
            result.append(char)
        else:
            if freq[char] < k:
                freq[char] += 1
                result[-1] += char
            else:
                return "NO"
    
    if len(result) != k:
        return "NO"
    
    return result

if __name__ == "__main__":
    k = int(input())
    q = input().strip()

    if is_beautiful_sequence_possible(k, q) == "NO":
        print("NO")
    else:
        print("YES")
        beautiful_sequence = generate_beautiful_sequence(k, q)
        for seq in beautiful_sequence:
            print(seq)
