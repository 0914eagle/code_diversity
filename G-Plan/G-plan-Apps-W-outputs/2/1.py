
def is_beautiful_sequence(k, q):
    freq = {}
    for c in q:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    if any(freq[c] > 1 for c in freq):
        return "NO"

    result = []
    start = 0
    for c in sorted(freq.keys()):
        end = start + freq[c]
        result.append(q[start:end])
        start = end

    if len(result) != k:
        return "NO"
    else:
        return "YES", result

if __name__ == "__main__":
    k = int(input())
    q = input().strip()
    answer = is_beautiful_sequence(k, q)
    if answer == "NO":
        print("NO")
    else:
        print("YES")
        for s in answer[1]:
            print(s)
