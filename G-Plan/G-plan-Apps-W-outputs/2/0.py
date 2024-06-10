eautiful_sequence_possible(k, q):
    freq = {}
    for char in q:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    if any(freq[char] >= k for char in freq):
        return "NO"
    
    beautiful_sequence = []
    current_char = None
    for char in q:
        if current_char != char:
            beautiful_sequence.append("")
            current_char = char
        beautiful_sequence[-1] += char
    
    return "YES", beautiful_sequence


if __name__ == "__main__":
    k = int(input())
    q = input().strip()
    
    result = is_beautiful_sequence_possible(k, q)
    if result == "NO":
        print("NO")
    else:
        print("YES")
        for seq in result[1]:
            print(seq