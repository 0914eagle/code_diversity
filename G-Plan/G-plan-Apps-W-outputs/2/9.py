
def is_beautiful_sequence_possible(k, q):
    if len(set(q)) < k:
        return "NO"
    
    first_chars = set()
    seq = []
    for char in q:
        if char not in first_chars:
            first_chars.add(char)
            seq.append(char)
            if len(seq) == k:
                break
    
    if len(seq) == k:
        return "YES", seq
    else:
        return "NO",

if __name__ == "__main__":
    k = int(input())
    q = input().strip()
    
    result = is_beautiful_sequence_possible(k, q)
    print(result[0])
    if result[0] == "YES":
        for s in result[1]:
            print(s)
