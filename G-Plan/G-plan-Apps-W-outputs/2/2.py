
def is_beautiful_sequence(k, q):
    chars = sorted(set(q))
    if len(chars) < k:
        return "NO"
    
    seq = []
    for i in range(k):
        seq.append(q[:q.find(chars[i])+1])
        q = q[q.find(chars[i])+1:]
    
    return "YES", seq

if __name__ == "__main__":
    k = int(input())
    q = input().strip()
    
    result = is_beautiful_sequence(k, q)
    if result == "NO":
        print("NO")
    else:
        print(result[0])
        for s in result[1]:
            print(s)
